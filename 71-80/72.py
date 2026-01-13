"""
Ejercicio 72
Crear una clase Circulo con los siguientes atributos:
*radio: radio del circulo
*__init__(self, radio): incializa los atributos
de la clase
*calcular_perimetro(self): calcula y
devuelve el perimetro del circulo
"""

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

circulo1 = Circulo(5)

print(f"Area: {circulo1.calcular_area()}")
print(f"Perimetro: {circulo1.calcular_perimetro()}")