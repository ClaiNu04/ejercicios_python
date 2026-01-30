"""
Ejercicio 98
Crear una funcion que cree un archivo
html que diga Hola Mundo
"""

def crear(nombre, contenido):
    with open(nombre, 'w') as archivo:
        archivo.write(contenido)

crear('index.html', "Hola Mundo")
