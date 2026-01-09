"""
Ejercicio 60
Calcular la suma de los números pares del 1 al 10
"""

numero = 0
for i in range(1, 11):
    if i % 2 == 0:
        numero += i

print(numero)

        