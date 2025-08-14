from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QApplication
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QSize, pyqtSignal, Qt


from Backend.SFunctions import coordToNum

from Backend.Pieces.Bishop import Bishop
from Backend.Pieces.Knight import Knight
from Backend.Pieces.Queen import Queen
from Backend.Pieces.Rook import Rook


class LeveleoPeon(QDialog):
    emitir = pyqtSignal(dict) # se conecta con el chess 
    def __init__(self,piece):
        super().__init__()
        self.setWindowTitle("Ascender Pieza")
        self.setGeometry(100,100,185,200)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowCloseButtonHint) # Deshabilitar el botón de cerrar 
        self.setModal(True)

        self.color = piece.getcolor()
        self.nombre = piece.getname()
        self.lugar = coordToNum(piece.getplace())

        self.torre = Rook(self.lugar[0], self.lugar[1], self.color, self.nombre)
        self.caballo = Knight(self.lugar[0], self.lugar[1], self.color, self.nombre)
        self.alfil = Bishop(self.lugar[0], self.lugar[1], self.color, self.nombre)
        self.reina = Queen(self.lugar[0], self.lugar[1], self.color, self.nombre)

        self.seleccionSpecialPiece()
        

    def seleccionSpecialPiece(self):
        # label
        etiquetaUsuario = QLabel(self)
        etiquetaUsuario.setText("Escoja la evolucion de ")
        etiquetaUsuario.setFont(QFont("Calibri",12))
        etiquetaUsuario.move(20,10)

        etiquetaUsuario = QLabel(self)
        etiquetaUsuario.setText(self.nombre)
        etiquetaUsuario.setFont(QFont("Calibri",12))
        etiquetaUsuario.move(40,25)

        # boton "Pieza1"
        boton1 = QPushButton(self)
        boton1.setObjectName("Torre")
        boton1.setIcon(QIcon(self.torre.getimage()))
        boton1.resize(65,65)
        boton1.setIconSize(QSize(57, 57))
        boton1.move(23,50)      
        boton1.clicked.connect(self.select)

        # boton "Pieza2"
        boton2 = QPushButton(self)
        boton2.setObjectName("Alfil")
        boton2.setIcon(QIcon(self.alfil.getimage()))
        boton2.resize(65,65)
        boton2.setIconSize(QSize(57, 57))
        boton2.move(93,50)
        boton2.clicked.connect(self.select)

        # boton "Pieza3"
        boton3 = QPushButton(self)
        boton3.setObjectName("Caballo")
        boton3.setIcon(QIcon(self.caballo.getimage()))
        boton3.resize(65,65)
        boton3.setIconSize(QSize(57, 57))
        boton3.move(23,120)      
        boton3.clicked.connect(self.select)

        # boton "Pieza4"
        boton4 = QPushButton(self)
        boton4.setObjectName("Reina")
        boton4.setIcon(QIcon(self.reina.getimage()))
        boton4.resize(65,65)
        boton4.setIconSize(QSize(57, 57))
        boton4.move(93,120)
        boton4.clicked.connect(self.select)
        
    def select(self):
        boton = self.sender()
        if boton.objectName() == "Torre":
            self.emitir.emit({'type': 'Rook', 'value': self.torre })

        elif boton.objectName() == "Alfil":
            self.emitir.emit({'type': 'Bishop', 'value': self.alfil })
        
        elif boton.objectName() == "Caballo":
            self.emitir.emit({'type': 'Knight', 'value': self.caballo })
        
        else:
            self.emitir.emit({'type': 'Queen', 'value': self.reina })

        self.accept()
    
