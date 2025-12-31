"""
Ejercicio 23
Verifica si una palabra es un palindromo
"""

palabra = "radar"
if palabra == palabra[::-1]:
    print("Es un palindromo")
else:
    print("No es un palindromo")