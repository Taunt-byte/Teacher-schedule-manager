
"""
Modelos de dados do Teacher Schedule Manager.

Define as entidades principais do sistema:
- Professores
- Disciplinas
- Turmas
- Salas
- Horários

Utiliza SQLAlchemy ORM para mapear as classes
Python para tabelas do banco SQLite.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Table,
    Time,
    UniqueConstraint
)

from sqlalchemy.orm import declarative_base, relationship


# Classe-base para todos os modelos.
Base = declarative_base()


# ============================================================
# RELACIONAMENTO ENTRE PROFESSORES E DISCIPLINAS
# ============================================================

teacher_subject = Table(
    "teacher_subject",
    Base.metadata,

    Column(
        "teacher_id",
        Integer,
        ForeignKey("teachers.id"),
        primary_key=True
    ),

    Column(
        "subject_id",
        Integer,
        ForeignKey("subjects.id"),
        primary_key=True
    )
)


# ============================================================
# PROFESSORES
# ============================================================

class Teacher(Base):
    """
    Representa um professor cadastrado no sistema.
    """

    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(120), nullable=False)

    email = Column(String(150), unique=True)

    phone = Column(String(20))

    active = Column(Boolean, default=True, nullable=False)

    # Disciplinas que o professor pode ministrar.
    subjects = relationship(
        "Subject",
        secondary=teacher_subject,
        back_populates="teachers"
    )

    # Aulas atribuídas ao professor.
    schedules = relationship(
        "ScheduleEntry",
        back_populates="teacher"
    )

    def __repr__(self):
        return f"<Teacher(name='{self.name}')>"


# ============================================================
# DISCIPLINAS
# ============================================================

class Subject(Base):
    """
    Representa uma disciplina acadêmica.
    """

    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(255))

    # Quantidade de aulas semanais por turma.
    weekly_hours = Column(Integer, default=2, nullable=False)

    teachers = relationship(
        "Teacher",
        secondary=teacher_subject,
        back_populates="subjects"
    )

    schedules = relationship(
        "ScheduleEntry",
        back_populates="subject"
    )

    def __repr__(self):
        return f"<Subject(name='{self.name}')>"


# ============================================================
# TURMAS
# ============================================================

class SchoolClass(Base):
    """
    Representa uma turma de uma instituição.
    """

    __tablename__ = "school_classes"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(80), nullable=False)

    grade = Column(String(50))

    shift = Column(String(30))

    number_of_students = Column(Integer, default=0)

    schedules = relationship(
        "ScheduleEntry",
        back_populates="school_class"
    )

    def __repr__(self):
        return f"<SchoolClass(name='{self.name}')>"


# ============================================================
# SALAS
# ============================================================

class Room(Base):
    """
    Representa uma sala de aula ou laboratório.
    """

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(80), nullable=False)

    capacity = Column(Integer, default=30)

    room_type = Column(String(50), default="Classroom")

    schedules = relationship(
        "ScheduleEntry",
        back_populates="room"
    )

    def __repr__(self):
        return f"<Room(name='{self.name}')>"


# ============================================================
# HORÁRIOS
# ============================================================

class ScheduleEntry(Base):
    """
    Representa uma aula em determinado dia e horário.

    Cada registro relaciona:
    - Um professor.
    - Uma disciplina.
    - Uma turma.
    - Opcionalmente, uma sala.
    """

    __tablename__ = "schedule_entries"

    id = Column(Integer, primary_key=True, index=True)

    day_of_week = Column(Integer, nullable=False)

    start_time = Column(Time, nullable=False)

    end_time = Column(Time, nullable=False)

    teacher_id = Column(
        Integer,
        ForeignKey("teachers.id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    school_class_id = Column(
        Integer,
        ForeignKey("school_classes.id"),
        nullable=False
    )

    room_id = Column(
        Integer,
        ForeignKey("rooms.id"),
        nullable=True
    )

    # Relacionamentos ORM.
    teacher = relationship(
        "Teacher",
        back_populates="schedules"
    )

    subject = relationship(
        "Subject",
        back_populates="schedules"
    )

    school_class = relationship(
        "SchoolClass",
        back_populates="schedules"
    )

    room = relationship(
        "Room",
        back_populates="schedules"
    )

    # Impede registros duplicados para a mesma turma
    # com o mesmo horário de início.
    __table_args__ = (
        UniqueConstraint(
            "school_class_id",
            "day_of_week",
            "start_time",
            name="uq_class_schedule"
        ),
    )

    def __repr__(self):
        return (
            f"<ScheduleEntry("
            f"day={self.day_of_week}, "
            f"start={self.start_time})>"
        )


# ============================================================
# INICIALIZAÇÃO DO BANCO
# ============================================================

def create_tables(engine):
    """
    Cria as tabelas caso ainda não existam.
    """

    Base.metadata.create_all(bind=engine)
