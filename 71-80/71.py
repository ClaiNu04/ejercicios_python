"""
Ejercicio 71
Crear una clase rectangulo con los siguientes atributos:

Base: base del rectangulo
altura : altura del rectangulo 
la clase debe tener los siguientes metodos:
** __init__(sefl, base, altura):
Inicializa los atributos de la clase
**calcular_area(self): que calcula el area del rectangulo
**calcular_perimetro(self): que calcula el perimetro del rectangulo
""" 


class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

rec1 = rectangulo(5, 3)
print(f"Area:{rec1.calcular_area()}")
print(f"Perimetro:{rec1.calcular_perimetro()}")