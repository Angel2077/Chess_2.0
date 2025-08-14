from PyQt6.QtWidgets import QPushButton
from os import path

from Backend.Piece import Piece

class Pawn (Piece):  # Peon
    def __init__(self, x, y, color, name):
        super().__init__(x, y, color, name)
        self.image = path.join(self.rutaimage, color + " pawn.png")
        self.evo = True

    def valid_moves(self, board):
        """Movimientos Validos para la pieza Rook"""
        moves = []
        direction = 1 if self.color == 'white' else -1

        aux = 1
        # Movimiento recto + ocurrencia por primera vez en movimiento
        while aux <= 2:
            # Posible en la primera vuelta y la primera vez que se mueve
            # Ingresa la segunda casilla
            if ((self.y == 2 and self.color == 'white') or (self.y == 7 and self.color == 'black'))and aux == 1:
                    direction += 1 if self.color == 'white' else -1

            boton = board.findChild(QPushButton, f"boton ({self.x},{self.y + direction})")

            if boton.icon().isNull() != True:
                # Posible en la segunda vuelta y la primera vez que se mueve
                # Si encuentra una pieza frente a ella, elimina la casilla siguiente 
                if len(moves) != 0:
                    moves.pop()
            else:
                moves.append(f"({self.x},{self.y + direction})")

            # Posible en la primera vuelta y la primera vez que se mueve
            # Pasa a ser la casilla
            if ((self.y == 2 and self.color == 'white') or (self.y == 7 and self.color == 'black'))and aux == 1:
                direction += 1 if self.color == 'black' else -1
            aux += 1

        # Matar enemigo en diagonal
        if self.x == 1: # Quitamos el comer hacia la izquierda
            specialMoves = [(self.x +1 ,self.y +direction)]
        elif self.x == 8: # Quitamos el comer hacia la derecha
            specialMoves = [(self.x -1 ,self.y +direction)]
        else:
            specialMoves = [(self.x -1 ,self.y +direction), (self.x +1 ,self.y +direction)]

        for dx, dy in specialMoves:
            boton = board.findChild(QPushButton, f"boton ({dx},{dy})")
            if boton.icon().isNull() != True: # verifica si hay una pieza en la ubicacion deseada
                # carga la lista de piezas del rival
                if board.jugadores[0].getcolor() == self.color:
                    lista = board.jugadores[1].getListPiezas()
                else:
                    lista = board.jugadores[0].getListPiezas()
                    
                for pieza in lista:
                    # compara si la pieza esta al servicio del rival
                    if pieza.getplace() == boton.objectName():
                        moves.append(f"({dx},{dy})")
                        
        return moves



                
                
                    