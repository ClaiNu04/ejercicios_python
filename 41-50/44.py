""
Ejercicio 44
Adivina el numero aleatorio entre el 1 y el 10
""


import random

numero_aleatorio = random.randint(1, 10)
numero_usuario = int(input("Adivina el numero: "))
intentos = 0

while True:
    intento = int(input("Adivina el numero: "))
    intentos = intentos + 1
    if intento == numero_aleatorio:
        print(f"Felicidades, adivinaste el numero en {intentos} intentos")
        break
