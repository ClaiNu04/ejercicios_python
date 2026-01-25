"""
Ejercicio 86
Pide al usuario que ingrese un numero
crea una funcion que calcule el cuadrado de ese numero
Utilizando lambda
"""

calculadora = lambda x : x**2   #Crea la funcion que recibe un valor y lo eleva al cuadrado

numero = int(input("Ingrese un numero: "))      #pide un numero al usuario

print(calculadora(numero))      #Pinta en pantalla la ejecucion de la funcion y le pasa el valor del numero