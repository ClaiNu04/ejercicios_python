"""
Ejercicio 73
Crear una clase Libro
Con los atributos: titulo, autor, editorial, y fecha de publicacion
utilizando un metodo constructor y accediendo a estos atributos
"""


class Libro:

    def __init__(self, titulo, autor, editorial, publicacion_date):

        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.publicacion_date = publicacion_date 

mi_libro = Libro("La espada en la piedra", "Goku", "Senadoedit", "2001")

print(mi_libro.__dict__)
