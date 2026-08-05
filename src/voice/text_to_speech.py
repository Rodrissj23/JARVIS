"""
Text To Speech mediante Piper TTS (ADR-010).

Convierte texto en audio y lo reproduce. La capa Voice nunca decide
qué texto debe generarse; solo lo sintetiza y lo reproduce.
"""

import io
import wave

import numpy as np
import sounddevice as sd
from piper import PiperVoice


class TextToSpeech:
    """Sintetiza y reproduce texto como voz usando Piper TTS local."""

    def __init__(self, model_path: str) -> None:
        self._voice = PiperVoice.load(model_path)

    def speak(self, text: str) -> None:
        """Sintetiza `text` y lo reproduce por el altavoz por defecto."""
        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as wav_file:
            self._voice.synthesize(text, wav_file)

        buffer.seek(0)
        with wave.open(buffer, "rb") as wav_file:
            frames = wav_file.readframes(wav_file.getnframes())
            sample_rate = wav_file.getframerate()

        samples = np.frombuffer(frames, dtype=np.int16)
        sd.play(samples, samplerate=sample_rate)
        sd.wait()
