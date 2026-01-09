"""
Ejercicio 62
Crea una funcion que calcule el area de un circulo dado el radio
"""

import math

def area_circulo(radio):
    return math.pi * radio ** 2

resultado = area_circulo(float(input("Ingresa el radio de tu circulo: ")))
print(resultado)