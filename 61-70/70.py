"""
Ejercicio 70
Escribe una funcion para clasificar si una sustancia es acida, neutra o alcalina
"""

def nivel_ph(ph):
    if ph == 7:
        return("El ph es neutro ")
    elif ph < 7:
        return("El ph es acido ")
    else:
        return("El ph es alcalido ")

resultado = nivel_ph(int(input("Escriba el nivel de ph: ")))
print(resultado)