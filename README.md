# Teacher Schedule Manager

**A desktop application for academic timetable management, developed in Python.**

Teacher Schedule Manager is an academic project focused on simplifying the creation, organization, and management of class schedules for educational institutions and individual teachers.

The application aims to provide tools for managing teachers, subjects, classrooms, and weekly timetables through a desktop interface, with both manual scheduling and automated timetable generation.

> **Project Status:** In Development

---

## Overview

Managing academic schedules can be a complex task, especially when dealing with multiple teachers, subjects, classrooms, and weekly time slots.

Teacher Schedule Manager aims to address this challenge by providing a centralized desktop application where users can organize academic information and create schedules while avoiding conflicts and respecting scheduling constraints.

The project is being developed in Python, with an emphasis on software architecture, database management, graphical interfaces, and algorithmic problem-solving.

## Features

### Planned Features

- [ ] **Teacher Management:** Register, edit, search, and remove teachers.
- [ ] **Subject Management:** Organize subjects and their weekly workload.
- [ ] **Class Management:** Create and manage academic classes and groups.
- [ ] **Classroom Management:** Register classrooms and laboratories.
- [ ] **Manual Scheduling:** Create and modify weekly timetables manually.
- [ ] **Automatic Scheduling:** Generate timetables using algorithms.
- [ ] **Conflict Detection:** Identify overlapping schedules and unavailable teachers.
- [ ] **Teacher Availability:** Define individual teacher availability.
- [ ] **Timetable Visualization:** Display schedules by teacher or class.
- [ ] **PDF Export:** Generate printable timetable reports.

## Technologies

The project uses the following technologies:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PySide6 | Desktop graphical interface |
| SQLite | Local database |
| SQLAlchemy | Object-relational mapping (ORM) |
| Alembic | Database migrations |
| ReportLab | PDF generation |
| pytest | Automated testing |
| PyInstaller | Desktop executable packaging |

## Project Architecture

The application follows a modular architecture, separating the graphical interface, database operations, business logic, and scheduling algorithms.

```text
teacher-schedule-manager/
│
├── src/
│   └── teacher_schedule/
│       ├── config/
│       ├── database/
│       ├── models/
│       ├── services/
│       ├── algorithms/
│       ├── ui/
│       └── resources/
│
├── tests/
├── data/
├── requirements.txt
└── README.md
```

## Scheduling Algorithms

One of the main technical challenges of this project is the automatic generation of academic timetables.

The scheduling system is planned to use constraint-based approaches to distribute classes while respecting rules such as:

- A teacher cannot teach two classes simultaneously.
- A classroom cannot be occupied by multiple classes at the same time.
- A class cannot attend two different subjects simultaneously.
- Weekly subject workloads must be respected.
- Teacher availability must be considered.

Algorithms such as **Backtracking**, **Greedy Search**, and potentially **Genetic Algorithms** will be explored during development.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Taunt-byte/Teacher-schedule-manager.git

cd teacher-schedule-manager
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

**Windows PowerShell:**

```powershell
$env:PYTHONPATH = "src"
python -m teacher_schedule.main
```

**Linux:**

```bash
PYTHONPATH=src python -m teacher_schedule.main
```

## Demonstration

Screenshots and demonstrations will be added as the graphical interface and main features become available.

| Dashboard | Weekly Timetable |
|---|---|
| Coming soon | Coming soon |

## Academic Context

This repository is part of an academic programming challenge proposed by **Carlos H. L. Feichas**, from Centro Universitário Salesiano de São Paulo (UNISAL), Lorena campus.

The project provides an opportunity to apply software engineering concepts and explore practical solutions to scheduling problems.

## Learning Objectives

Throughout development, this project aims to explore:

- Object-oriented programming with Python.
- Desktop application development with PySide6.
- Relational database modeling and ORM.
- Software architecture and modular development.
- Algorithm design and constraint satisfaction problems.
- Automated testing and code organization.
- Data validation and scheduling optimization.

## License

This project is developed for academic and educational purposes.

A license will be defined before public distribution.

---

**Developed by Lucas Neves da Silva**

*Computer Engineering Student | UNISAL Lorena*