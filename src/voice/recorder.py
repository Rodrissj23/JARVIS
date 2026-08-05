"""
Captura de audio desde el micrófono.

Según docs/01_ARCHITECTURE.md, la capa Voice únicamente captura audio.
No decide qué hacer con la solicitud del usuario; esa decisión
corresponde al Orchestrator.
"""

import numpy as np
import sounddevice as sd


class AudioRecorder:
    """Graba audio desde el micrófono por defecto del sistema."""

    def __init__(self, sample_rate: int = 16000, channels: int = 1) -> None:
        self._sample_rate = sample_rate
        self._channels = channels

    @property
    def sample_rate(self) -> int:
        return self._sample_rate

    def record(self, duration_seconds: float) -> np.ndarray:
        """Graba audio durante `duration_seconds` segundos.

        Devuelve un array float32 mono a `sample_rate`, listo para
        ser transcripto por SpeechToText.
        """
        audio = sd.rec(
            int(duration_seconds * self._sample_rate),
            samplerate=self._sample_rate,
            channels=self._channels,
            dtype="float32",
        )
        sd.wait()
        return audio.flatten()
