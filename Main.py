import sys
import os

# Agregar las carpetas al sistema de rutas (Mayor facilidad al codificar)
directorios = ["Frontend","Backend","Assets"]
for carpeta in directorios:
    ruta = os.path.abspath(os.path.join(os.path.dirname(__file__), carpeta))
    sys.path.append(ruta)

# Importar el menu
from Frontend import Menu
Menu.Ejecute()

# Dev
# from Frontend import Chess
# Chess.play()
