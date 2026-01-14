"""
Ejercicio 75
Crea una clase Coche con los atributos:
- Marca:
- Modelo:
- Modelo:
- Matricula:
- Kilometros:
Crea un metodo __init__ como constructor y un metodo avanzar que
aumente el kilometraje del coche
"""

class Coche:
    
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km

    def avanzar(self, km):
            self.km = self.km + km

coche1 = Coche("nissan", "delta", "HK-1990", 1)

coche1.avanzar(3)
print(coche1.__dict__)

