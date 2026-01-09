"""
Ejercicio 64
Crea una funcion que revise si un numero es par o impar
"""

print("Este es un programa que chequea si un numero es par o impar")

def chequeo(numero):
    if numero % 2 == 0:
        print("Es un numero par")
    elif numero % 2 != 0:
        print("El numero no es par")
        return 
chequeo(int(input("Numero a chequear: ")))