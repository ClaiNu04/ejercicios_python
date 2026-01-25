"""
Ejercicio 81
Elevar una lista de numero utilizando el 
operador map()
"""

def cuadrados(x):
    return x**2

numeros = [1,2,3,5,9,12]

cuadrados = (list(map(cuadrados, numeros)))

print(numeros)
print(cuadrados)