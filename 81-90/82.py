"""
Ejercicio 82
Convertir una lista de cadenas de numeros a enteros utilizando map()
"""

def convertir(cadena):
    return int(cadena)

cadenas = ["1", "3", "4", "6", "9"]

enteros = list(map(convertir, cadenas))

print(cadenas)
print(enteros)