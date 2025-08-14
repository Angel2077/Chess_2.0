from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton 
from PyQt6.QtCore import Qt, pyqtSignal


class OptionsWindow(QDialog):
    emitir = pyqtSignal(bool) # se conecta con el chess 
    def __init__(self, x, y, ventana):
        super().__init__()
        self.ventana = ventana
        self.setWindowTitle("Opciones")
        self.setGeometry(x+100, y+100, 400, 300)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Etiqueta principal
        label = QLabel("Opciones", self)
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

        # Botón para volver al menú principal
        back_button = QPushButton("Volver al juego", self)
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
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)
    
    def cerrar(self):
        self.close() and self.ventana.back()