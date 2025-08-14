def coordToNum(string:str):
    """Transforma un String con forma de coordenadas a una lista de numeros"""
    if string.startswith("boton"):
        string = string.replace("boton ", "")
    lista = string.replace("(", "").replace(")", "").split(",")
    res:list = []
    for aux in range(len(lista)):
        if lista[aux] == "0":
            res.append(0)
        elif lista[aux] == "1":
            res.append(1)
        elif lista[aux] == "2":
            res.append(2)
        elif lista[aux] == "3":
            res.append(3)
        elif lista[aux] == "4":
            res.append(4)
        elif lista[aux] == "5":
            res.append(5)
        elif lista[aux] == "6":
            res.append(6)
        elif lista[aux] == "7":
            res.append(7)
        elif lista[aux] == "8":
            res.append(8)
        elif lista[aux] == "9":
            res.append(9)
    return res

def numToLetter(number:int):
    """Transforma un Numero a una letra mayuscula"""
    if 0 < number < 27:
        return chr(number + 64)
    else:
        print("Error: Fuera de Rango")
        return
    
def calcularSize(tamaño:int, elem:int, val:int = None):
    """Calcula los tamaños para centrar perfectamente una "caja" horizontal o vertical\n
    val: valor para que se posicione mas de un lado (+) u otro (-)"""
    if tamaño > elem:
        res = (tamaño - elem) // 2
        print(res)
        if val != None and tamaño != elem:
                res = res + val // 2
                if res >= 0:
                    return res
                return 0
        return res
    else:
        print("Error: el Tamaño es menor que el Elemento")
        return 0
