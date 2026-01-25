"""
Ejercicio 90
Imprimir los dobles de una lista de numero utilizando map y lambda
"""

import math

numeros = [1, 3, 6, 4, 5]
duplicados = list(map(lambda x : x*2, numeros))

print(duplicados)