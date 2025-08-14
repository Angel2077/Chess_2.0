from PyQt6.QtWidgets import QDialog, QPushButton, QLabel
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QSize, pyqtSignal, Qt

from Backend.Musica import Music

class RPGWindow(QDialog):
    emitir = pyqtSignal(dict) # se conecta con el chess 
    def __init__(self,p1,p2,x,y):
        super().__init__()
        self.setGeometry(x + 100,y + 100,400,300)
        self.setWindowTitle("Battle")
        self.musica = Music()
        self.musica.play_battle_music()
        self.p1 = p1
        self.p2 = p2
        self.setModal(True)
        # Deshabilitar el botón de cerrar 
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowCloseButtonHint)
        self.quienVive()

    def quienVive(self):
        

        # componentes para ingresar usuarios
        # label
        etiquetaUsuario = QLabel(self)
        etiquetaUsuario.setText("Quien gana?")
        etiquetaUsuario.setFont(QFont("Calibri",12))
        etiquetaUsuario.move(130,100)

        # boton "Pieza1"
        boton1 = QPushButton(self)
        boton1.setObjectName("Pieza 1")
        boton1.setIcon(QIcon(self.p1.getimage()))
        boton1.resize(60,60)
        boton1.setIconSize(QSize(55, 55))
        boton1.move(150,200)      
        boton1.clicked.connect(self.ganador)

        # boton "Pieza2"
        boton2 = QPushButton(self)
        boton2.setObjectName("Pieza 2")
        boton2.setIcon(QIcon(self.p2.getimage()))
        boton2.resize(60,60)
        boton2.setIconSize(QSize(55, 55))
        boton2.move(250,200)
        boton2.clicked.connect(self.ganador)
        
    def ganador(self):
        boton = self.sender()
        if boton.objectName() == "Pieza 1":
            self.emitir.emit({'type': 'bool', 'value': True })
        else:
            self.emitir.emit({'type': 'bool', 'value': False })
        self.accept()
