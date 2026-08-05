"""
Módulo Hora.

Según docs/01_ARCHITECTURE.md, cada módulo implementa una capacidad
independiente y no se comunica directamente con Brain, UI ni Voice.
Su interfaz pública es `can_handle` y `handle`, invocadas por el
Orchestrator (docs/05_TASKS.md - TASK-007), que es quien decide si
esta solicitud le corresponde a este módulo o debe derivarse a Brain.
"""

from datetime import datetime

_KEYWORDS = ("hora",)


class HoraModule:
    """Responde solicitudes relacionadas con la hora actual."""

    def can_handle(self, text: str) -> bool:
        """Indica si este módulo puede resolver `text`."""
        return any(keyword in text.lower() for keyword in _KEYWORDS)

    def handle(self, text: str) -> str:
        """Devuelve la hora actual.

        Debe llamarse únicamente cuando `can_handle(text)` es `True`.
        """
        return f"Son las {datetime.now().strftime('%H:%M')}."
