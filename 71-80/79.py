"""
Ejercicio 79
Representa una cuenta de banco con de posito y retiro
y que tenga los atributos:
Titular y saldo 
Utiliza POO:
"""

class Cuenta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, cantidad):
        self.saldo += cantidad
    
    def retiro(self, cantidad):
        self.saldo -= cantidad

    def mostrar(self):
        print(self.__dict__)


cuenta1 = Cuenta('Clai', 500)  #saldo incial de la cuenta
cuenta1.mostrar()
cuenta1.deposito(200) #deposito dejando el saldo en 700$
cuenta1.mostrar()
cuenta1.retiro(700) #retiro de 700$ que deja la cuenta en 0$
cuenta1.mostrar()
