from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton 
from PyQt6.QtCore import Qt, pyqtSignal
from Backend.Musica import Music


class WinWindow(QDialog):
    emitir = pyqtSignal(bool) # se conecta con el chess 
    def __init__(self,ganador, x, y, ventana):
        super().__init__()
        self.musica = Music()
        self.musica.play_game_over_music()
        self.ventana = ventana
        self.setWindowTitle("Opciones")
        self.setGeometry(x+100, y+100, 100, 200)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta principal
        label = QLabel(f"Jugador {ganador} Gano esta contienda", self)
        label.setStyleSheet("font-size: 24px; color: #333;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
        # Botón para volver al menú principal
        back_button = QPushButton("Volver al menu", self)
        back_button.setStyleSheet("""
            QPushButton {
                font-size: 18px; 
                padding: 10px; 
                background-color: rgba(200,0,0,255); 
                color: white;
            }
            QPushButton:hover {
                background-color: #ef6c00;
            }
        """)
        back_button.clicked.connect(self.cerrar)
        layout.addWidget(back_button)

    def cerrar(self):
        self.close() and self.ventana.back()