"""
Pedir un año y mostrar si es bisiesto
regla: 
    -divisible entre 4
    -no divisible entre 100
    -divisible entre 400
"""

año = int(input("Ingrese un numero: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
