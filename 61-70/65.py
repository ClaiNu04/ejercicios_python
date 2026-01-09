"""
Ejercicio 65
Crea una funcion que convierta grados celcius a farenheit
"""


def celsius_farenheit(grados):
    return (grados * 9/5) + 32

resultado = celsius_farenheit(int(input("Cuantos grados celcius convertira a farenheit?: ")))
print(resultado)