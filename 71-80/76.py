"""
Ejercicio 76
Crea un clase animal con los atributos:
-Especie y nombre
Crea dos metodos el metodo constructor
- __init__ y otro metodo hablar que haga que 
segun la raza diga 'guau' si es perro y 'miau' si es gato
"""


class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        if self.especie == 'perro':
            print("guau")
        elif self.especie == 'gato':
            print('miau')
        else:
            print('...')
        

animal1 = Animal("perro", "Docki")
animal2 = Animal("gato", "michi")

animal1.hablar()
animal2.hablar()