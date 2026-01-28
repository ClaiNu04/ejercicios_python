"""
Ejercicio 91
Crea una funcion que le pases una lista de numeros
y te devuelva los que son pares utilizando filter()
"""

numeros = [1, 3, 4, 8, 4, 1, 2, 3, 6, 10]

pares = list(filter(lambda x : x %2 == 0, numeros))

print(numeros)
print(pares)

