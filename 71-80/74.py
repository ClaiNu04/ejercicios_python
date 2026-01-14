"""
Ejercicio 74
Crea una clase persona con los atributos:
- Nombre
- Edad
- DNI
Crea un metodo que calcule si esa persona es mayor de edad o no
"""


class Persona:
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        
persona1 = Persona(f"Juan", 20, "433-3400339-1")

print("El nombre de la persona es: ",persona1.nombre)

if persona1.es_mayor_de_edad():
    print(persona1.nombre, "es mayor de edad")