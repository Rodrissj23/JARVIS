"""
Ventana principal de JARVIS.

Contiene únicamente la ventana base de la interfaz gráfica.
Los estados visuales y las animaciones se implementarán en una tarea
posterior (ver docs/05_TASKS.md - TASK-003).

Según docs/01_ARCHITECTURE.md, la UI nunca debe contener lógica de negocio.
"""

from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación JARVIS."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("JARVIS")
        self.resize(800, 600)