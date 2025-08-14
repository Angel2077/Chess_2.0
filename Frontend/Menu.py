from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtWidgets  import QComboBox, QStackedWidget
from PyQt6.QtCore import Qt, QTimer 
import sys
from Frontend.Chess import ChessBoardWidget
from Backend.Musica import Music

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG-Chess MainWindow")
        # minimo x = 800, minimo y = 600
        self.winX = 800
        self.winY = 600
        self.posX = 100
        self.posY = 100
        self.setGeometry(self.posX, self.posY, self.winX, self.winY)  # Resolución predeterminada
        # Limitamos la resolucion
        self.setMaximumSize(self.winX, self.winY) 
        self.setMinimumSize(self.winX, self.winY)

        self.menu = Menu(self.winX, self.winY,self.posX, self.posY, self)
        self.setCentralWidget(self.menu)
        self.show()

    def back(self):
        self.menu = Menu(self.winX, self.winY,self.posX, self.posY, self)
        self.setCentralWidget(self.menu)
        self.show()
                
class Menu(QWidget):
    def __init__(self, tx, ty, px, py, parent):
        super().__init__()
        self.windo = parent
        self.winX = tx
        self.winY = ty
        self.posX = px
        self.posY = py
        self.musica = Music()
        self.musica.play_menu_music()
        self.vVentana = QStackedWidget(self) # Creamos un "stack" de widgets
        self.vVentana.setGeometry(0, 0, tx, ty)
        # Cargamos los widgets
        self.menu()
        self.create_options_page()
        self.pantallaCarga()
        
    def menu(self):
        # Página principal del menú
        menu = QWidget()
        layout = QVBoxLayout()
        layout.setObjectName("Menu")
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Título del juego
        title_label = QLabel("Chess Game RPG", self)
        title_label.setStyleSheet("font-size: 36px; color: #333;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Etiqueta principal
        label = QLabel("¡Bienvenido al Juego!", self)
        label.setStyleSheet("font-size: 24px; color: #333;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Botón para iniciar el juego
        start_game_button = QPushButton("Iniciar Juego", self)
        start_game_button.setObjectName("Inicio")
        start_game_button.setStyleSheet("""
            QPushButton {
                font-size: 18px; 
                padding: 10px; 
                background-color: #4CAF50; 
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        start_game_button.clicked.connect(self.action)
        layout.addWidget(start_game_button)

        # Botón para ir al menú de opciones
        options_button = QPushButton("Opciones", self)
        options_button.setObjectName("Opciones")
        options_button.setStyleSheet("""
            QPushButton {
                font-size: 18px; 
                padding: 10px; 
                background-color: #2196F3; 
                color: white;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        options_button.clicked.connect(self.action)
        layout.addWidget(options_button)

        # Botón para salir
        exit_button = QPushButton("Salir", self)
        exit_button.setStyleSheet("""
            QPushButton {
                font-size: 18px; 
                padding: 10px; 
                background-color: #f44336; 
                color: white;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        exit_button.clicked.connect(sys.exit)  # Cierra la aplicación
        layout.addWidget(exit_button)
        
        menu.setLayout(layout)
        self.vVentana.addWidget(menu)

    def create_options_page(self):
        # Página de opciones
        option = QWidget()
        layout = QVBoxLayout(option)
        layout.setObjectName("Opciones")
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta principal
        label = QLabel("Opciones", self)
        label.setStyleSheet("font-size: 24px; color: #333;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Configuración de resolución
        resolution_label = QLabel("Resolución:", self)
        resolution_label.setStyleSheet("font-size: 18px;")
        layout.addWidget(resolution_label)

        self.resolution_dropdown = QComboBox(self)
        self.resolution_dropdown.addItems(["800x600","1024x768","1280x960","1440x1080"])
        self.resolution_dropdown.setCurrentText("800x600")  # Predeterminado
        self.resolution_dropdown.currentIndexChanged.connect(self.change_resolution)
        layout.addWidget(self.resolution_dropdown)

        # Botón para volver al menú principal
        back_button = QPushButton("Volver al Menú Principal", self)
        back_button.setObjectName("Volver")
        back_button.setStyleSheet("""
            QPushButton {
                font-size: 18px; 
                padding: 10px; 
                background-color: #f57c00; 
                color: white;
            }
            QPushButton:hover {
                background-color: #ef6c00;
            }
        """)
        back_button.clicked.connect(self.action)
        layout.addWidget(back_button)

        option.setLayout(layout)
        self.vVentana.addWidget(option)        

    def change_resolution(self):
        # Cambiar la resolución de la ventana principal
        resolution = self.resolution_dropdown.currentText()
        width, height = map(int, resolution.split("x"))

        self.windo.setMaximumSize(width, height) 
        self.windo.setMinimumSize(width, height) 
        self.winX = width
        self.winY = height
        
        self.windo.setGeometry(self.windo.x(), self.windo.y(), width, height)
        self.vVentana.setGeometry(0, 0, width, height)

    def pantallaCarga(self):
        # Pagina que simula pantalla de carga
        
        carga = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(150,150,150,150)
        
        loading_label = QLabel("Cargando, por favor espera...", self)
        loading_label.setStyleSheet("font-size: 24px;")
        layout.addWidget(loading_label)

        carga.setLayout(layout)
        self.vVentana.addWidget(carga) 

    def start_loading(self):
        self.game = ChessBoardWidget(self.winX, self.winY, self.posX, self.posY, self.windo)
        self.vVentana.hide() # Ocultamos los widgets
        self.windo.setCentralWidget(self.game)
        self.game.show()

    def action(self):
        # Cambiamos el widget principal a conveniencia del guion
        btn = self.sender()
        if btn.objectName() == "Volver":
            self.vVentana.setCurrentIndex(0) 
        elif btn.objectName() == "Opciones":
            self.vVentana.setCurrentIndex(1)
        elif btn.objectName() == "Inicio":
            # pantalla de carga para evitar sospechas xd
            self.musica.stopmusic()
            del self.musica
            self.vVentana.setCurrentIndex(2)
            timer = QTimer(self) 
            timer.singleShot(100,self.start_loading)

class Ejecute():
    def __init__(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        app.exec()
