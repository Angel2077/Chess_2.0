from PyQt6.QtWidgets import QPushButton
from os import path

from Backend.Piece import Piece

class King (Piece): # Rey
    def __init__(self, x, y, color, name):
        super().__init__(x, y, color, name)
        self.image = path.join(self.rutaimage, color + " king.png")

    def valid_moves(self, board):
        """Movimientos Validos para la pieza King"""
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),  # Linea recta
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]  # Diagonales
        
        for dx, dy in directions:
            x, y = self.x + dx, self.y + dy

            if 1 <= x <= 8 and 1 <= y <= 8: # Limitar el rango de la pieza al tablero
                boton = board.findChild(QPushButton, f"boton ({x},{y})")

                if boton.icon().isNull() != True: # verifica si hay una pieza en la ubicacion deseada
                    # carga la lista de piezas del rival
                    if board.jugadores[0].getcolor() == self.color:
                        lista = board.jugadores[1].getListPiezas()
                    else:
                        lista = board.jugadores[0].getListPiezas()

                    for pieza in lista:
                        # compara si la pieza esta al servicio del rival
                        if pieza.getplace() == boton.objectName():
                            moves.append(f"({x},{y})")
                else:
                    moves.append(f"({x},{y})")
                    
        return moves
