"""
Brain de JARVIS.

Según docs/01_ARCHITECTURE.md, el Brain es responsable de la
comunicación con Claude, la construcción del contexto y la recepción
de respuestas. Nunca interactúa directamente con la UI ni con Voice,
y nunca ejecuta acciones del sistema.

Toda comunicación con el resto del sistema se realiza a través del
Orchestrator, que es quien posee la instancia de Brain (ver
src/orchestrator/orchestrator.py). Esta clase no decide el flujo ni
el estado de JARVIS; solo construye el contexto de la conversación,
lo envía a Claude y devuelve la respuesta.

Requiere la variable de entorno ANTHROPIC_API_KEY configurada
(decisión tomada durante TASK-006). El SDK oficial de Anthropic la
detecta automáticamente al crear el cliente.
"""

from typing import Dict, List

import anthropic

DEFAULT_MODEL = "claude-sonnet-5"
DEFAULT_MAX_TOKENS = 1024


class Brain:
    """Comunica JARVIS con Claude, manteniendo el contexto de la conversación."""

    def __init__(self, model: str = DEFAULT_MODEL) -> None:
        self._model = model
        self._client = None
        self._history: List[Dict[str, str]] = []

    def _get_client(self) -> anthropic.Anthropic:
        """Crea el cliente de Anthropic la primera vez que se solicita
        (lazy loading), siguiendo el mismo patrón que SpeechToText usa
        para cargar el modelo de Whisper.
        """
        if self._client is None:
            self._client = anthropic.Anthropic()
        return self._client

    def ask(self, text: str) -> str:
        """Envía `text` a Claude junto con el historial de la conversación
        y devuelve la respuesta como texto.

        El historial se mantiene en memoria mientras la instancia de
        Brain exista, permitiendo que la conversación tenga contexto
        entre turnos.
        """
        self._history.append({"role": "user", "content": text})

        response = self._get_client().messages.create(
            model=self._model,
            max_tokens=DEFAULT_MAX_TOKENS,
            messages=self._history,
        )

        reply = response.content[0].text
        self._history.append({"role": "assistant", "content": reply})
        return reply
