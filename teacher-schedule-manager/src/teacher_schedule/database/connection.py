"""
Gerenciamento da conexão com o banco de dados.

Este módulo configura o SQLAlchemy e fornece
sessões para operações com o banco SQLite.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from teacher_schedule.config.settings import DATABASE_URL


# Criação do mecanismo de conexão com o SQLite.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)


# Fábrica de sessões do banco de dados.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_session():
    """
    Cria e disponibiliza uma sessão do banco.

    A sessão deve ser encerrada após sua utilização.
    """

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()