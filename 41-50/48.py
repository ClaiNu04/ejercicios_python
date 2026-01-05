"""
Ejercicio 48
Crea un programa que simule el lanzamiento de una moneda.
"""


import random

while True:
    moneda = random.randint(0, 1)
    if moneda == 0:
        print("Cara")
    else:
        print("Cruz")
    jugar = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar == "n":
        break