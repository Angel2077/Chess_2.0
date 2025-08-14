from PyQt6.QtWidgets import QPushButton
from os import path

from Backend.Piece import Piece

class Queen(Piece): # Reina
    def __init__(self, x, y, color, name):
        super().__init__(x, y, color, name)
        self.image = path.join(self.rutaimage, color + " queen.png")

    def valid_moves(self, board):
        """Movimientos Validos para la pieza Bishoop"""
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),  # linea recta
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]  # en diagonal
        
        for dx, dy in directions:
            x, y = self.x, self.y
            rev = True # Inidicador que cambia cuando se en cuentra una pieza  
            while rev:
                x += dx
                y += dy
                
                if (1 <= x <= 8) and (1 <= y <= 8): # Limitar el rango de la pieza al tablero
                    boton = board.findChild(QPushButton, f"boton ({x},{y})")
                    rev = boton.icon().isNull() # si no tiene icono = true
                    if  rev != True:
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
                else:
                    rev = False
                    
        return moves
