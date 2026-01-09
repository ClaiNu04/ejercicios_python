""" 
Ejercicio 68
Escriba una funcion que pida distancia y velocidad y que calcule el tiempo de viaje
"""

def tiempo(distancia, velocidad ):
    return distancia / velocidad
    
distancia = float(input("Distancia que recorrio: "))
velocidad = float(input("Velociad a la que se desplazo: "))
print(tiempo(distancia, velocidad))


