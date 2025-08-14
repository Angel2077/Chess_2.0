import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

from Backend.Player import Player
from Backend.SFunctions import coordToNum
from Backend.Musica import Music

from Frontend.Rpg import RPGWindow
from Frontend.LeveleoPeon import LeveleoPeon
from Frontend.options import OptionsWindow
from Frontend.Win import WinWindow


# Clase que carga lo necesario para jugar
class ChessBoardWidget(QWidget):

    def __init__(self, px, py, tx, ty, ventana):
        super().__init__()
        # resolucion de pantalla
        self.winX = px
        self.winY = py
        self.posX = tx
        self.posY = ty 
        self.ventana = ventana
        self.init_board()
        self.init_option()
        self.init_pieces()
        self.musica()
        

    def init_option(self):
        self.option = QPushButton(self) 
        self.option.setObjectName("Opciones")
        self.option.move(self.winX - (self.sizes // 2 + 10), 10)
        self.option.resize((self.sizes // 2), (self.sizes // 2))
        self.option.clicked.connect(self.opciones)
    
    # Crea el tablero
    def init_board(self):
        self.sizes = self.winY // 8
        # tablero 8x8
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                # Casillas del tablero
                button = QPushButton(self) 
                button.setObjectName(f"boton ({col + 1},{row + 1})")
                button.resize(self.sizes,self.sizes)
                button.move(self.sizes * (col) , self.sizes * (7 - row))
                button.setStyleSheet("""QPushButton { border: 2px solid #8f8f91; 
                                     background-color: %s; 
                                     color: white; 
                                     padding: 10px; } 
                                     QPushButton:pressed { 
                                     background-color: %s; } """%(color,color))
                button.clicked.connect(self.push)

                # Botones que serviran para mover las piezas
                actionbtn = QPushButton(self)
                actionbtn.setObjectName(f"({col + 1},{row + 1})")
                actionbtn.resize(self.sizes,self.sizes)
                actionbtn.move(self.sizes * (col) , self.sizes * (7 - row))
                actionbtn.setStyleSheet(""" QPushButton { 
                                        background-color: rgba(0,255,0,128) ; 
                                        border: 2px solid #000000; 
                                        border-radius: 30px; 
                                        } 
                                        QPushButton:hover { 
                                        background-color: rgba(0,255,0,192); 
                                        }
                                        QPushButton:pressed { 
                                        background-color: rgba(0,255,0,255); 
                                        }""")
                actionbtn.clicked.connect(self.mover)
                actionbtn.setDisabled(True)
                actionbtn.setHidden(True)

        # Boton que cancelara el movimiento
        self.cancel = QPushButton(self)
        self.cancel.setObjectName("Cancel")
        self.cancel.resize(self.sizes,self.sizes)
        self.cancel.setStyleSheet(""" QPushButton { 
                                  background-color: rgba(255,0,0,128) ; 
                                  border: 2px solid #000000; 
                                  border-radius: 30px; /* Radio de borde para hacerlo redondeado */ 
                                  } 
                                  QPushButton:hover { 
                                  background-color: rgba(255,0,0,192); 
                                  }
                                  QPushButton:pressed { 
                                  background-color: rgba(255,0,0,255); 
                                  }""")
        self.cancel.clicked.connect(self.cancelar)
        self.cancel.setDisabled(True)
        self.cancel.setHidden(True)

    # Crea las piezas en base a los Jugadores (matando a 2 pajaros de un tiro)
    def init_pieces(self):
        # Creacion y almacenamiento de los jugadores
        jugador1 = Player(1)
        jugador2 = Player(2)
        self.jugadores = [jugador1, jugador2]
        self.jugadorActivo = self.jugadores[0] # Asignamos el jugador activo (Blanco por defecto xd) 
        size = self.sizes // 15 * 13
        for jujalag in self.jugadores:
            lista = jujalag.getListPiezas()
            for pieza in lista:
                boton = self.findChild(QPushButton, pieza.getplace())
                boton.setIcon(QIcon(pieza.getimage())) # Cargamos la imagen de cada pieza
                boton.setIconSize(QSize( size , size )) # Ajustar el tamaño de la imagen

    # cargamos la musica
    def musica(self):
        self.music = Music()
        self.music.play_tablero_music()

    # Agrega la funcionalidad de las piezas
    def push(self):
        boton = self.sender() # Detecta que boton se pulso
        if boton.icon().isNull() != True:
            lista = self.jugadorActivo.getListPiezas()
            for pieza in lista:
                if pieza.getplace() == boton.objectName(): # Busca si la pieza esta en la lista del jugador activo
                    self.music.play_move_effect()
                    moves = pieza.valid_moves(self)
                    self.selectpiece = coordToNum(pieza.getplace()) # Guarda temporalmente la ubicacion de la pieza seleccionada
                    self.seleccion(moves, self.selectpiece[0], self.selectpiece[1])

    # Muestra los posibles movimientos de la pieza escogida
    def seleccion(self, lista, x, y):
        # Desabilita todas las casillas del tablero
        for row in range(8):
            for col in range(8):
                botonM = self.findChild(QPushButton, f"boton ({col + 1},{row + 1})")
                botonM.setDisabled(True)

        # Habilita y Muestra los botones de accion con base a la lista de movimientos disponibles de la pieza
        for cord in lista:
            btn = self.findChild(QPushButton, cord)
            btn.setHidden(False)
            btn.setDisabled(False)
        
        # habilita y Muestra el boton "Cancel en el mismo lugar de la pieza"
        self.cancel.move(self.sizes * (x-1) , self.sizes * (8 - y))
        self.cancel.setDisabled(False)
        self.cancel.setHidden(False)

    # Intenta mover la pieza al lugar escogido o morira en el intento xd
    def mover(self):
        # Jugador Rival
        if self.jugadores[0] != self.jugadorActivo:
               rival = self.jugadores[0]
        else:
               rival = self.jugadores[1]

        # Posicion iniciada
        x = self.selectpiece[0]
        y = self.selectpiece[1]
        del self.selectpiece

        # Botones
        botonINI = self.findChild(QPushButton, (f"boton ({x},{y})"))
        botonINT = self.sender()
        botonFIN = self.findChild(QPushButton, (f"boton {botonINT.objectName()}"))

        # Posicion Deseada
        new = coordToNum(botonINT.objectName())
        x = new[0]
        y = new[1]

        # Pieza Bulleadora
        activeP = self.jugadorActivo.getPieza(botonINI.objectName())

        # Pieza Bulleada
        if botonFIN.icon().isNull() != True:
            rivalP = rival.getPieza(botonFIN.objectName())
        else:
            rivalP = None

        if rivalP == None: 
            self.res = True 
        else:
            # Cortamos la musica
            # self.music.stopmusic()
            # del self.music

            # Entra al modo rpg
            # self.rpg = RPGWindow(activeP,rivalP,self.posX, self.posY)
            # self.rpg.emitir.connect(self.respuesta) # actua si recibe un cambio en otra ventana
            # self.rpg.exec() 
            # del self.rpg

            
            # self.musica() # Volvemos a cargar la musica


            # Gana el atacante (chess original)
            self.res = True

            # Gana el atacado
            # self.res = False
        size = self.sizes // 15 * 13
        self.music.play_move_effect()

        if self.res:
            # Empieza a cambiar el icono de la casilla, y la posicion interna de la pieza
            botonFIN.setIcon(botonINI.icon())
            botonFIN.setIconSize(QSize(size, size))
            botonINI.setIcon(botonINT.icon())
            activeP.setplace(x,y)
            if rivalP != None:
                rival.modPiezas(rivalP,2) # Directo a la lista de los renegados
                self.res = True
                if rivalP.getname().count("Rey"):
                    self.win = WinWindow(self.jugadorActivo.getname(), self.posX, self.posY, self.ventana)
                    self.res = False
                    self.win.exec() 

        else:
            # Deja de ser utilizable la pieza escogida del jugador activo
            self.jugadorActivo.modPiezas(activeP,2) # Directo a la lista de los renegados
            botonINI.setIcon(botonINT.icon()) 

        self.cancelar()
        
        if self.res:
            # Chequeos para ascender al Peon
            peonblanco = (activeP.getcolor() == "white" and y == 8 and activeP.getname().count("Peon") == 1 and activeP.getevo())
            peonnegro = (activeP.getcolor() == "black" and y == 1 and activeP.getname().count("Peon") == 1 and activeP.getevo())
            if peonblanco or peonnegro:
                ascenderPeon = LeveleoPeon(activeP)
                ascenderPeon.emitir.connect(self.respuesta) # actua si recibe un cambio en otra ventana
                ascenderPeon.exec() 
                del ascenderPeon

                # Comienza el ascenso del peon
                botonFIN.setIcon(QIcon(self.res.getimage()))
                botonFIN.setIconSize(QSize(size, size))

                self.jugadorActivo.modPiezas(activeP, 3)
                self.jugadorActivo.modPiezas(self.res, 1)
        del self.res
        self.jugadorActivo = rival # Cambio de turno
        
    # Guarda temporalmente la variable de la otra ventana
    def respuesta(self,data):
        self.res = data['value'] 
        return

    # Regresa todo a la normalidad
    def cancelar(self):
        for row in range(8):
            for col in range(8):
                # Habilita las casillas del tablero
                boton = self.findChild(QPushButton, f"boton ({col + 1},{row + 1})")
                boton.setEnabled(True)
                # Deshabilita  y oculta los botones de accion
                boton = self.findChild(QPushButton, f"({col + 1},{row + 1})")
                boton.setHidden(True)
                boton.setDisabled(True)
        
        # Deshabilita  y oculta el boton "Cancel"
        self.cancel.setDisabled(True)
        self.cancel.setHidden(True)
    
    def opciones(self):
        self.option = OptionsWindow(self.ventana.x(), self.ventana.y(), self.ventana) 
        self.option.emitir.connect(self.cerrar) # actua si recibe un cambio en otra ventana
        self.option.exec() 

    def cerrar(self, value):
        self.ventana.change()
        
# Test
class play():
    def __init__(self):
        app = QApplication(sys.argv)
        ventana = ChessWindow()
        sys.exit(app.exec())


# Clase que crea la ventana
class ChessWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPGChess")
        winX = 800
        winY = 600
        posX = 100
        posY = 100        
        self.setGeometry(posX, posY, winX, winY)
        self.setMaximumSize(winX, winY)
        self.setMinimumSize(winX, winY)
        self.board_widget = ChessBoardWidget(winX, winY, posX, posY ,self)
        self.setCentralWidget(self.board_widget)  # colocamos como principal
        self.show()
