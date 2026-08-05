"""
Estados oficiales de JARVIS.

Definidos en docs/02_CORE_FLOW.md. Este módulo únicamente declara los
estados posibles; la decisión de cuándo transicionar entre ellos es
responsabilidad del Orchestrator, no de la UI.
"""

from enum import Enum


class JarvisState(Enum):
    """Estados oficiales de JARVIS."""

    INICIALIZANDO = "Inicializando"
    REPOSO = "Reposo"
    ESCUCHANDO = "Escuchando"
    PROCESANDO = "Procesando"
    HABLANDO = "Hablando"
    ERROR = "Error"