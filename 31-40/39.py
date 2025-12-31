"""
Pedir una palabra y mostrar si es la correcta
"""


palabra = input("Ingrese una palabra: ")

palabra = palabra.lower()

if palabra == "codigo":
    print("Correcto")
else:
    print("Incorrecto")