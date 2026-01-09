"""
Ejercicio 67 
Crea una formula que calcule el volumen de un cilindro
"""

import math

def volumen(radio, altura):
    return math.pi * radio ** 2 * altura

radio = float(input("El radio es: "))
altura = float(input("La altura es: "))
print(volumen(radio, altura))