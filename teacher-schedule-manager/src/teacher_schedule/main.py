
"""
Ponto de entrada do Teacher Schedule Manager.

Inicializa o banco de dados e executa
a aplicação desktop utilizando PySide6.
"""

import sys

from PySide6.QtWidgets import QApplication

from teacher_schedule.database.connection import engine
from teacher_schedule.database.models import create_tables

from teacher_schedule.ui.main_window import MainWindow


def main():
    """
    Executa a aplicação.
    """

    # Inicializa as tabelas do banco.
    create_tables(engine)

    # Cria a aplicação Qt.
    app = QApplication(sys.argv)

    # Cria a janela principal.
    window = MainWindow()

    # Exibe a interface.
    window.show()

    # Inicia o loop de eventos.
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
