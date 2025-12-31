"""
Ejercicio 35
Pedir un numero y mostrar si esta entre 1 y 50
"""

numero = int(input("Ingrese un numero: "))

if numero in range(1, 50):
    print("El numero esta entre 1 y 50")
else:
    print("El numero no esta entre 1 y 50")
    