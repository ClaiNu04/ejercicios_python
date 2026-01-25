"""
Ejercicio 84
Obtener el cuadrado de dos lista de numeros sumados
"""

def sumar_listas(x, y):
    return (x + y)**2

lista1 = [1, 2, 3, 4]
lista2 = [4, 2, 2, 1]

lista_resultado = list(map(sumar_listas, lista1, lista2))
print(lista_resultado)