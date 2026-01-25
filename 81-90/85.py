"""
Ejercicio 85
Contar el numero de vocales en una lista 
de palabras utilizando map()
"""

def contar_vocales(palabra):
    vocales = "aeiou"
    return sum(1 for letra in palabra if letra.lower() in vocales)

palabras = ["Hola", "Mundo", "Python", "Hi"]
vocales_contadas = list(map(contar_vocales, palabras))

print(vocales_contadas)