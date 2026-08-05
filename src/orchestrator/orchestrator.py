"""
Orchestrator de JARVIS.

Según docs/01_ARCHITECTURE.md, el Orchestrator es el corazón del
sistema: recibe todas las solicitudes, decide qué módulo utilizar y
controla el estado de JARVIS. Ningún otro componente decide el flujo;
esa responsabilidad es exclusiva del Orchestrator.

Esta implementación (TASK-005) construye la estructura del
Orchestrator, define su interfaz pública y prepara los puntos de
comunicación con UI, Voice, Brain y Modules.

No incluye lógica de conversación ni ejecución de acciones del
sistema: la integración real con Brain (Claude) corresponde a
TASK-006, y el registro de módulos funcionales a TASK-007/TASK-008.
Por eso `brain` y `modules` quedan preparados pero sin utilizarse
todavía.
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
