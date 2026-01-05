"""
Ejercicio 49
Crea un programa que simule el lanzamiento de un dado hasta que salga un 6.
"""

import random

while True:
    dado = random.randint(1, 6)
    print(dado)
    if dado == 6:
        break
    jugar = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar == "n":
        break