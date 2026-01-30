"""
Ejercicio 97
Hacer una funcion para crear un archivo 
de texto plano
"""

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w'):
        pass

crear_archivo('index.html')