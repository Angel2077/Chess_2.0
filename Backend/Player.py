from .Pieces.Bishop import Bishop
from .Pieces.King import King
from .Pieces.Knight import Knight
from .Pieces.Pawn import Pawn
from .Pieces.Queen import Queen
from .Pieces.Rook import Rook

class Player(): # Jugador
    def __init__(self,n): # n: Numero del jugador
        self.piezasj = [] # lista de piezas vivas
        self.sacadasj = [] # lista de piezas comidas
        self.name = str(n)
        if n == 1:
            
            self.color = "white"
        elif n == 2:
            self.color = "black"
        self.createPiezas()

    def createPiezas(self):
        """Crea las piezas con sus devidas clases y las guarda en una lista interna"""
        # Base de la Ubicacion de las piezas especiales
        x = 1
        y = 1 if self.color == "white" else 8

        laux = [" Torre_1" , " Caballo_1" , " Alfil_1" , " Reina" , " Rey" , " Alfil_2" , " Caballo_2" , " Torre_2"] # Nombres de las piezas

        for name in laux: 
            if name.startswith(" T"):   # Torre
                pieza = Rook(x,y,self.color, self.color + name)

            elif name.startswith(" C"): # Caballo
                pieza = Knight(x,y,self.color, self.color + name)

            elif name.startswith(" A"): # Alfil
                pieza = Bishop(x,y,self.color, self.color + name)

            elif name.endswith("ey"):   # Rey
                pieza = King(x,y,self.color, self.color + name)

            else:                       #Reina
                pieza = Queen(x,y,self.color, self.color + name)

            self.piezasj.append(pieza)
            x += 1
 
        # Base de la Ubicacion de los peones
        x = 1
        y += 1 if self.color == "white" else -1

        laux = [" Peon_1", " Peon_2", " Peon_3", " Peon_4", " Peon_5", " Peon_6", " Peon_7", " Peon_8"] # Nombes de los peones

        for name in laux: 
            pieza = Pawn(x,y,self.color, self.color + name)
            self.piezasj.append(pieza)
            x += 1
        
    def modPiezas(self,elem,acc):
        """1 = agregar a la lista de vivos.\n 
        2 = mueve a la lista de los comidos.\n
        3 = elimina de la lista de los vivos.\n"""
        if acc == 1: # agregar
            self.piezasj.append(elem)
        elif acc == 2: # mover a la lista de renegados
            if self.piezasj.count(elem) != 0:
                index = self.piezasj.index(elem)
                pieza = self.piezasj.pop(index)
                self.sacadasj.append(pieza)
            else:
                print("ERROR: Valor no encontrado")
            return
        elif acc == 3: #elimina la pieza de los vivos
            if self.piezasj.count(elem) != 0:
                index = self.piezasj.index(elem)
                self.piezasj.pop(index)
            else:
                print("ERROR: Valor no encontrado")
            return
        else:
            print("ERROR: Metodo erroneo")
        return
    
    def getListPiezas(self):
        return self.piezasj
    
    def getcolor(self):
        return self.color
    
    def getPieza(self,coordenadas:str):
        """Obtiene la pieza requerida ingresando sus coordenadas"""
        if coordenadas.startswith("boton") != True:
            coordenadas = "boton " + coordenadas

        for pieza in self.piezasj:
            if pieza.getplace() == coordenadas:
                return pieza
        print("ERROR: Valor no encontrado")
        return 
    
    def getname(self):
        return self.name
    
class testplayer():
    if __name__ == "__main__":
        jugador1 = Player(1)
        piezas = jugador1.getListPiezas()
        piezas[0].setplace(2,2)
        pieza = jugador1.getPieza("boton "+ "(2,2)")
        print(pieza)
        print(piezas[0].getplace())
