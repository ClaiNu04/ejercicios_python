"""
Ejercicio 93
Filtrar numeros negativos de una lista utilizando filter
"""

numeros = [-1, -6, 3, 4, -9, 10, -11]
numeros_negativos = list(filter(lambda x : x < 0, numeros))

print(numeros)
print(numeros_negativos)