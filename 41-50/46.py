"""
Ejercicio 46
Contar la cantidad de digitos de un numero ingresado por el usuario
"""
numero = int(input("Ingrese un numero: "))
contador = 0

while numero != 0:
    numero = numero // 10
    contador += 1

print(f"El numero tiene {contador} digitos")