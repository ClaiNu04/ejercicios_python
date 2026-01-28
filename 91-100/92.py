"""
Ejercicio 92
Filtrar cadenas de longitud mayor que 3 en una lista
usando filter()
"""

lista = ['clai', 'robert', 'sol', 'un', 'de', 'mi']

palabras_largas = list(filter(lambda x : len(x) >= 3, lista)) 

print(lista)
print(palabras_largas)