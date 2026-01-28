"""
Ejercicio 95
Filtrar elementos de una lista que sean lista
"""

lista = [['12', '13'], 7, 2.3, ['clai', 18]]

lista_filtrada= list(filter(lambda x: isinstance(x, list), lista))

print(lista)
print(lista_filtrada)