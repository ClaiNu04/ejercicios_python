"""
Ejercicio 42
Suma de los primeros numeros
"""

numero = int(input("Ingrese un numero: "))
suma = 0
i = 1
while i <= numero:
    suma += i
    i += 1

print("La suma de los numeros es:", suma)