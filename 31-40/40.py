"""
Ejercicio 40
Calcular el IMC
"""

peso = float(input("Ingrese su peso en kg: "))
talla = float(input("Ingrese su talla en metros: "))

imc = peso / (talla ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc < 24.9:
    print("Normal")
elif imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")