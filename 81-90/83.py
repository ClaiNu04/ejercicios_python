"""
Ejercicio 83
Calcular la longitud de una lista de palabras utilizando map()
"""

def contar_palabra(palabra):
    return len(palabra)

palabras = ["hola", 'que tal', 'super', 'Python']
conteo = list(map(contar_palabra, palabras))

print(palabras)
print(conteo)