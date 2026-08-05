"""
Ventana principal de JARVIS.

Contiene la ventana base de la interfaz gráfica y la representación
visual de los estados de JARVIS mediante un núcleo/reactor central
(ADR-008).

Según docs/01_ARCHITECTURE.md, la UI nunca debe contener lógica de negocio:
esta ventana solo muestra el estado que se le indique mediante `set_state`,
no decide cuándo cambiar de estado. Esa decisión es responsabilidad del
Orchestrator (ver docs/05_TASKS.md - TASK-004 y siguientes).
"""

from PySide6.QtGui import QColor, QPainter, QPaintEvent, QPen
from PySide6.QtWidgets import QMainWindow, QWidget

from src.ui.states import JarvisState

_STATE_COLORS = {
    JarvisState.INICIALIZANDO: "#5A5A5A",
    JarvisState.REPOSO: "#1E3A5F",
    JarvisState.ESCUCHANDO: "#00A8E8",
    JarvisState.PROCESANDO: "#F4A300",
    JarvisState.HABLANDO: "#2ECC71",
    JarvisState.ERROR: "#E74C3C",
}

_RING_COLOR = "#FFFFFF"
_RING_WIDTH = 6


class _ReactorCore(QWidget):
    """Núcleo/reactor central: círculo con anillo que representa el estado.

    Solo pinta el color que se le indique mediante `set_color`.
    No decide ni contiene lógica sobre cuándo cambiar de color.
    """

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self._color = QColor(_STATE_COLORS[JarvisState.INICIALIZANDO])

    def set_color(self, color: str) -> None:
        self._color = QColor(color)
        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        side = max(min(self.width(), self.height()) - _RING_WIDTH * 2, 0)
        x = (self.width() - side) // 2
        y = (self.height() - side) // 2

        pen = QPen(QColor(_RING_COLOR))
        pen.setWidth(_RING_WIDTH)
        painter.setPen(pen)
        painter.setBrush(self._color)
        painter.drawEllipse(x, y, side, side)


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación JARVIS."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("JARVIS")
        self.resize(800, 600)

        self._core = _ReactorCore(self)
        self.setCentralWidget(self._core)

        self.set_state(JarvisState.INICIALIZANDO)

    def set_state(self, state: JarvisState) -> None:
        """Actualiza la representación visual del estado actual de JARVIS."""
        self._core.set_color(_STATE_COLORS[state])