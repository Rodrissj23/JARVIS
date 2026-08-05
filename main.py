"""
JARVIS - Punto de entrada principal.

Instancia y conecta los componentes principales del sistema (UI,
Voice, Brain, Orchestrator), registra los módulos iniciales y deja
preparado el flujo de comunicación a través del Orchestrator
(docs/05_TASKS.md - TASK-009).

La ejecución continua y la detección de palabra de activación no
están incluidas todavía: quedan fuera del alcance de esta tarea.

La ruta del modelo de voz de Piper se lee desde la variable de
entorno JARVIS_TTS_MODEL_PATH, cargada mediante un archivo .env local
(decisión tomada durante TASK-009), para no dejarla fija en el código.
"""

import os
import sys

from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication

from src.brain.brain import Brain
from src.modules.clima import ClimaModule
from src.modules.fecha import FechaModule
from src.modules.hora import HoraModule
from src.orchestrator.orchestrator import Orchestrator
from src.ui.main_window import MainWindow
from src.ui.states import JarvisState
from src.voice.voice_engine import VoiceEngine


def _get_tts_model_path() -> str:
    """Lee la ruta del modelo de voz de Piper desde la configuración
    externa (.env), sin dejarla fija en el código.
    """
    load_dotenv()
    model_path = os.environ.get("JARVIS_TTS_MODEL_PATH")
    if not model_path:
        raise RuntimeError(
            "Falta configurar JARVIS_TTS_MODEL_PATH en el archivo .env "
            "con la ruta al modelo de voz de Piper."
        )
    return model_path


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    voice = VoiceEngine(_get_tts_model_path())
    brain = Brain()

    orchestrator = Orchestrator(ui=window, voice=voice, brain=brain)
    orchestrator.register_module("hora", HoraModule())
    orchestrator.register_module("fecha", FechaModule())
    orchestrator.register_module("clima", ClimaModule())

    # Fin de la carga: JARVIS pasa a estado de reposo (docs/02_CORE_FLOW.md).
    orchestrator.set_state(JarvisState.REPOSO)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()