"""
Ejercicio 78
Crea una clase persona y otra clase estudiante 
La clase persona tiene el atributo nombre y el metodo
mostrar_nombre()
La clase estudiante debe heredar de la clase persona y utilizar el metodo
mostrar_nombre() de la clase persona
"""

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def mostrar(self):
        super().mostrar_nombre()