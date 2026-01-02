"""
Ejercicio 43
Pide un numero y calcula su factorial
"""

numero = int(input("Ingrese un numero: "))
factorial = 1
i = 1
while i <= numero:
    factorial *= i
    i += 1
print("El factorial de", numero, "es", factorial)