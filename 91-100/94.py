"""
Ejercicio 94
Filtrar cadenas que tengan un caracter especifico
"""

cadenas = ['apple', 'python', 'amstar', 'vino', 'bien']
caracter = 'a'

filtro = list(filter(lambda x: caracter in x, cadenas))

print(cadenas)
print(filtro)