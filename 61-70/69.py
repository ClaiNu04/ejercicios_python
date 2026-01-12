"""
Ejercicio 69
Escribe una funcion que calcule la tasa de desempleo
"""

def tasa_desempleo(no_em, si_em):
    return (no_em / si_em) * 100

resultado = tasa_desempleo(100, 900)

print(resultado)