"""
Orchestrator de JARVIS.

Según docs/01_ARCHITECTURE.md, el Orchestrator es el corazón del
sistema: recibe todas las solicitudes, decide qué módulo utilizar y
controla el estado de JARVIS. Ningún otro componente decide el flujo;
esa responsabilidad es exclusiva del Orchestrator.

Esta implementación (TASK-005) construyó la estructura del
Orchestrator y su interfaz pública, preparando los puntos de
comunicación con UI, Voice, Brain y Modules.

TASK-007 agregó `handle_request`, el punto único que decide si una
solicitud la resuelve un módulo registrado o, si ninguno aplica, se
deriva a Brain. Los módulos nunca acceden directamente a Brain, UI o
Voice: su interfaz pública es `can_handle(text)` y `handle(text)`.
"""

from typing import Any, Dict, Optional

from src.ui.states import JarvisState


class Orchestrator:
    """Punto único de coordinación del sistema."""

    def __init__(
        self,
        ui: Optional[Any] = None,
        voice: Optional[Any] = None,
        brain: Optional[Any] = None,
    ) -> None:
        """
        ui: componente de interfaz gráfica. Debe exponer `set_state`
            (ver src/ui/main_window.py).
        voice: instancia de la capa Voice (ver
            src/voice/voice_engine.py). Reservada para uso futuro.
        brain: reservado para la futura integración con Claude
            (TASK-006). No se utiliza todavía.
        """
        self._ui = ui
        self._voice = voice
        self._brain = brain
        self._modules: Dict[str, Any] = {}
        self._state = JarvisState.INICIALIZANDO

    @property
    def state(self) -> JarvisState:
        """Estado actual de JARVIS."""
        return self._state

    def set_state(self, state: JarvisState) -> None:
        """Actualiza el estado de JARVIS y lo refleja en la UI.

        Este es el único punto del sistema que decide y controla el
        estado de JARVIS (docs/01_ARCHITECTURE.md - Orchestrator). La
        UI únicamente representa visualmente el estado que se le
        indica; no decide cuándo cambiar (docs/02_CORE_FLOW.md).
        """
        self._state = state
        if self._ui is not None:
            self._ui.set_state(state)

    def register_module(self, name: str, module: Any) -> None:
        """Registra un módulo bajo un nombre único.

        Prepara el punto de comunicación con Modules para TASK-007 y
        TASK-008. Ningún módulo se registra todavía.
        """
        self._modules[name] = module

    def handle_request(self, text: str) -> str:
        """Resuelve una solicitud de texto.

        Consulta `can_handle(text)` de cada módulo registrado; el
        primero que devuelva `True` resuelve la solicitud mediante su
        `handle(text)`. Si ningún módulo aplica, la solicitud se
        deriva a Brain. Este es el único punto del sistema que decide
        qué módulo utilizar (docs/01_ARCHITECTURE.md - Orchestrator).
        """
        for module in self._modules.values():
            if module.can_handle(text):
                return module.handle(text)

        if self._brain is not None:
            return self._brain.ask(text)

        raise RuntimeError(
            "Ningún módulo pudo resolver la solicitud y no hay Brain configurado."
        )