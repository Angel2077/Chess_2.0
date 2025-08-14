from abc import ABC, abstractmethod
from os import path

class Piece:
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.name = name
        self.place = f"boton ({x},{y})" # Facilidad de ubicar en el tablero (conjunto de botones)
        self.color = color  # Blanco o negro para las piezas
        self.evo = False # Capacidad de evolucionar

        self.rutaimage = path.abspath(path.join(path.dirname(__file__), '../Assets/Piezas')) # ruta donde estan las imagenes
        self.image = "" # Nombre de la imagen representativa

        # Atributos base para el RPG
        self.hp = 100
        self.damage = 10
        self.defense = 5  # Pasar como metodo abstracto para heredar en rpg

    @abstractmethod
    def valid_moves(self, board):
        # para que cada pieza tenga su propia logica de movimiento esto es herencia
        pass

    def getimage(self):
        return self.image

    def getplace(self):
        return self.place
    
    def setplace(self,x, y):
        self.x = x
        self.y = y
        self.place = f"boton ({x},{y})"
    
    def getname(self):
        return self.name
    
    def getcolor(self):
        return self.color
    
    def getevo(self):
        return self.evo
    
    def setevo(self, elem):
        self.evo = elem
    
    # Metodos RPG
    def is_alive(self):
        return self.hp > 0

    def receive_damage(self, damage):
        effective_damage = max(0, damage - self.defense)
        self.hp -= effective_damage
        print(
            f"{self.__class__.__name__} recibió {effective_damage} de daño. HP restante: {self.hp}")
        