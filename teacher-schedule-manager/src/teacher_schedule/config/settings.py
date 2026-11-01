"""
Configurações gerais do Teacher Schedule Manager.

Centraliza caminhos e configurações utilizadas
pelos diferentes módulos da aplicação.
"""

from pathlib import Path


# Diretório principal da aplicação no computador.
APP_DIRECTORY = Path.home() / ".teacher_schedule_manager"

# Cria o diretório caso ele ainda não exista.
APP_DIRECTORY.mkdir(parents=True, exist_ok=True)

# Caminho do banco de dados SQLite.
DATABASE_PATH = APP_DIRECTORY / "teacher_schedule.db"

# URL de conexão utilizada pelo SQLAlchemy.
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

# Informações gerais.
APP_NAME = "Teacher Schedule Manager"
APP_VERSION = "0.1.0"