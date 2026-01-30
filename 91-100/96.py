"""
Ejercicio 96
Crear una excepcion que me ayude a determinar
si el indice en una lista esta fuera del rango
"""

lista = [1, 2, 3]

try:
    print(lista[5])
except IndexError:
    print('Error el indice no existe')
