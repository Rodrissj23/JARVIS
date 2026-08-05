"""
JARVIS - Punto de entrada principal.

Este archivo es el punto de arranque de la aplicación.
Por ahora únicamente inicializa y muestra la ventana principal.
El resto de la inicialización (Voice, Orchestrator, Brain, Modules)
se implementará en tareas futuras.
"""

import sys

from PySide6.QtWidgets import QApplication

from src.ui.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()