"""
Ejercicio 31
Pide un numero y muestra si es negativo, cero o positivo
"""


numero = int(input("Ingrese un numero: "))

if numero < 0:
    print("El numero es negativo")
elif numero == 0:
    print("El numero es cero")
else:
    print("El numero es positivo")
