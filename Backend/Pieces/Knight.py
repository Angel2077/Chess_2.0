from PyQt6.QtWidgets import QPushButton
from os import path

from Backend.Piece import Piece

class Knight (Piece):  # Caballo
    def __init__(self, x, y, color, name):
        super().__init__(x, y, color, name)
        self.image = path.join(self.rutaimage, color + " knight.png")
        
    def valid_moves(self, board):
        """Movimientos Validos para la pieza Knight"""
        moves = []
        jumps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        for dx, dy in jumps:
            x, y = self.x + dx, self.y + dy

            if 1 <= x <= 8 and 1 <= y <= 8:  # Limitar el rango de la pieza al tablero
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
