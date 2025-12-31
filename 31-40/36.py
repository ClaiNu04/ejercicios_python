"""
Ejercicio 36
Pedir un caracter y mostrar si es una vocal
"""


caracter = input("Ingrese un caracter: ")   
vocales = "aeiou"

if caracter.lower() in vocales:
    print("El caracter es una vocal")
else:
    print("El caracter no es una vocal")