"""
Motor de voz de JARVIS.

Punto de entrada único de la capa Voice (docs/01_ARCHITECTURE.md).
Combina captura de audio, Speech To Text (ADR-009) y Text To Speech
(ADR-010). No contiene lógica de decisión: únicamente escucha y habla
cuando se le solicita.

Nota: la detección de palabra de activación descrita en
docs/02_CORE_FLOW.md todavía no está implementada. Requiere una
decisión de arquitectura sobre qué motor utilizar (ver
docs/05_TASKS.md - TASK-004).
"""

from typing import Callable, Optional

import numpy as np

from src.voice.recorder import AudioRecorder
from src.voice.speech_to_text import SpeechToText
from src.voice.text_to_speech import TextToSpeech

# Función sin argumentos que devuelve el audio capturado, para permitir
# futuras estrategias de captura (ej. detección de silencio) sin
# modificar la interfaz de `listen`.
AudioCapture = Callable[[], np.ndarray]

DEFAULT_LISTEN_DURATION_SECONDS = 5.0


class VoiceEngine:
    """Interfaz única de la capa Voice para el resto del sistema."""

    def __init__(self, tts_model_path: str) -> None:
        self._recorder = AudioRecorder()
        self._stt = SpeechToText()
        self._tts = TextToSpeech(tts_model_path)

    def listen(
        self,
        duration_seconds: float = DEFAULT_LISTEN_DURATION_SECONDS,
        capture: Optional[AudioCapture] = None,
    ) -> str:
        """Captura audio del usuario y lo devuelve transcripto como texto.

        Por defecto graba durante `duration_seconds` (comportamiento
        actual, sin cambios). Opcionalmente se puede pasar `capture`,
        una función sin argumentos que devuelva el audio a transcribir,
        dejando la interfaz preparada para futuras estrategias de
        captura sin acoplar `listen` a una duración fija.
        """
        audio = capture() if capture is not None else self._recorder.record(duration_seconds)
        return self._stt.transcribe(audio)

    def speak(self, text: str) -> None:
        """Reproduce `text` como voz."""
        self._tts.speak(text)