"""
Speech To Text mediante Whisper (ADR-009).

Convierte audio capturado en texto. La capa Voice nunca decide qué
hacer con el resultado; esa decisión corresponde al Orchestrator.
"""

import numpy as np
import whisper

DEFAULT_MODEL_NAME = "base"


class SpeechToText:
    """Transcribe audio a texto usando Whisper de forma local.

    El modelo se carga de forma diferida (lazy loading): no se carga
    al construir el objeto, sino recién la primera vez que se necesita
    transcribir. El nombre del modelo es configurable mediante
    `model_name`, sin quedar fijado en la implementación.
    """

    def __init__(self, model_name: str = DEFAULT_MODEL_NAME) -> None:
        self._model_name = model_name
        self._model = None

    def _get_model(self):
        """Carga el modelo la primera vez que se solicita (lazy loading)."""
        if self._model is None:
            self._model = whisper.load_model(self._model_name)
        return self._model

    def transcribe(self, audio: np.ndarray, language: str = "es") -> str:
        """Transcribe un array de audio (float32, 16kHz mono) a texto."""
        result = self._get_model().transcribe(audio, language=language)
        return result["text"].strip()