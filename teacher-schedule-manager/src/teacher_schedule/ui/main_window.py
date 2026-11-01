
"""
Janela principal do Teacher Schedule Manager.

Responsável por:
- Construir a interface principal.
- Criar o menu lateral.
- Controlar a navegação entre páginas.
- Apresentar o dashboard inicial.
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QFrame
)

from PySide6.QtCore import Qt

from teacher_schedule.config.settings import (
    APP_NAME,
    APP_VERSION
)


class MainWindow(QMainWindow):
    """
    Janela principal da aplicação.
    """

    def __init__(self):
        super().__init__()

        # Configurações da janela.
        self.setWindowTitle(f"{APP_NAME} - v{APP_VERSION}")
        self.resize(1200, 750)
        self.setMinimumSize(950, 600)

        # Inicializa a interface.
        self.setup_ui()

    def setup_ui(self):
        """
        Constrói a estrutura visual da aplicação.
        """

        # Widget central.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal.
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Menu lateral.
        self.sidebar = self.create_sidebar()

        # Área de conteúdo.
        self.content = QStackedWidget()

        # Criação das páginas.
        self.pages = {
            "Dashboard": self.create_dashboard(),
            "Professores": self.create_placeholder("Professores"),
            "Disciplinas": self.create_placeholder("Disciplinas"),
            "Turmas": self.create_placeholder("Turmas"),
            "Salas": self.create_placeholder("Salas"),
            "Horários": self.create_placeholder("Grade de Horários")
        }

        # Adiciona as páginas ao componente de navegação.
        for page in self.pages.values():
            self.content.addWidget(page)

        # Adiciona os componentes ao layout.
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content)

        # Apresenta o dashboard inicialmente.
        self.navigate_to("Dashboard")

        # Aplica o estilo visual.
        self.apply_styles()

    def create_sidebar(self):
        """
        Cria o menu lateral de navegação.
        """

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(230)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(15, 25, 15, 20)
        layout.setSpacing(12)

        # Nome do sistema.
        title = QLabel("TEACHER\nSCHEDULE")
        title.setObjectName("sidebar_title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)

        subtitle = QLabel("MANAGEMENT SYSTEM")
        subtitle.setObjectName("sidebar_subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(subtitle)

        layout.addSpacing(30)

        # Opções do menu.
        menu_items = [
            "Dashboard",
            "Professores",
            "Disciplinas",
            "Turmas",
            "Salas",
            "Horários"
        ]

        self.menu_buttons = {}

        for item in menu_items:

            button = QPushButton(item)

            button.setCursor(Qt.CursorShape.PointingHandCursor)

            button.setObjectName("menu_button")

            # Cada botão abre uma página específica.
            button.clicked.connect(
                lambda checked=False, name=item:
                self.navigate_to(name)
            )

            layout.addWidget(button)

            self.menu_buttons[item] = button

        layout.addStretch()

        # Informações da versão.
        version = QLabel(f"Version {APP_VERSION}")
        version.setObjectName("version_label")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(version)

        return sidebar

    def create_dashboard(self):
        """
        Cria o painel inicial da aplicação.
        """

        page = QWidget()

        layout = QVBoxLayout(page)
        layout.setContentsMargins(35, 30, 35, 30)
        layout.setSpacing(20)

        # Cabeçalho.
        title = QLabel("Dashboard")
        title.setObjectName("page_title")

        description = QLabel(
            "Bem-vindo ao Teacher Schedule Manager."
        )

        description.setObjectName("page_description")

        layout.addWidget(title)
        layout.addWidget(description)

        # Indicadores iniciais.
        indicators_layout = QHBoxLayout()

        indicators = [
            ("Professores", "0"),
            ("Disciplinas", "0"),
            ("Turmas", "0"),
            ("Horários", "0")
        ]

        for name, value in indicators:

            card = self.create_stat_card(name, value)

            indicators_layout.addWidget(card)

        layout.addLayout(indicators_layout)

        # Área de apresentação.
        information = QLabel(
            "Gerencie professores, disciplinas, turmas "
            "e horários em um único lugar.\n\n"
            "Comece cadastrando os dados da sua instituição."
        )

        information.setObjectName("information_card")

        information.setAlignment(Qt.AlignmentFlag.AlignCenter)

        information.setMinimumHeight(220)

        layout.addWidget(information)

        layout.addStretch()

        return page

    def create_stat_card(self, title, value):
        """
        Cria um cartão de estatística do dashboard.
        """

        card = QFrame()
        card.setObjectName("stat_card")

        layout = QVBoxLayout(card)

        title_label = QLabel(title)
        title_label.setObjectName("stat_title")

        value_label = QLabel(value)
        value_label.setObjectName("stat_value")

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        return card

    def create_placeholder(self, page_name):
        """
        Cria páginas temporárias para módulos ainda
        não implementados.
        """

        page = QWidget()

        layout = QVBoxLayout(page)

        layout.setContentsMargins(35, 30, 35, 30)

        title = QLabel(page_name)
        title.setObjectName("page_title")

        message = QLabel(
            f"O módulo de {page_name.lower()} será "
            "implementado nas próximas etapas."
        )

        message.setObjectName("page_description")

        layout.addWidget(title)
        layout.addWidget(message)

        layout.addStretch()

        return page

    def navigate_to(self, page_name):
        """
        Alterna entre as páginas da aplicação.
        """

        page = self.pages.get(page_name)

        if page is None:
            return

        self.content.setCurrentWidget(page)

        # Atualiza o estado visual do menu.
        for name, button in self.menu_buttons.items():

            button.setProperty(
                "active",
                name == page_name
            )

            # Força a atualização do estilo.
            button.style().unpolish(button)
            button.style().polish(button)

    def apply_styles(self):
        """
        Define a identidade visual da aplicação.
        """

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F4F6FA;
            }

            #sidebar {
                background-color: #17243A;
            }

            #sidebar_title {
                color: white;
                font-size: 21px;
                font-weight: bold;
            }

            #sidebar_subtitle {
                color: #91A2B9;
                font-size: 9px;
                letter-spacing: 2px;
            }

            #menu_button {
                background-color: transparent;
                color: #CBD5E1;
                border: none;
                border-radius: 7px;
                padding: 12px;
                text-align: left;
                font-size: 13px;
            }

            #menu_button:hover {
                background-color: #293B56;
                color: white;
            }

            #menu_button[active="true"] {
                background-color: #6654C7;
                color: white;
                font-weight: bold;
            }

            #version_label {
                color: #8291A7;
                font-size: 10px;
            }

            #page_title {
                color: #17243A;
                font-size: 27px;
                font-weight: bold;
            }

            #page_description {
                color: #718096;
                font-size: 13px;
            }

            #stat_card {
                background-color: white;
                border: 1px solid #E4E9F0;
                border-radius: 10px;
                min-height: 110px;
            }

            #stat_title {
                color: #718096;
                font-size: 12px;
            }

            #stat_value {
                color: #6654C7;
                font-size: 28px;
                font-weight: bold;
            }

            #information_card {
                background-color: white;
                border: 1px solid #E4E9F0;
                border-radius: 12px;
                color: #718096;
                font-size: 14px;
            }
        """)
