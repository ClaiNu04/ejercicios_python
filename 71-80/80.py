"""
Ejercicio 80
Obtener la memoria ram de tu computadora 
recuerda instalar la biblioteca externa psutil
con el comando: pip install psutil
"""

import psutil

def mostrar_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total/ (1024 ** 3)
    return memoria_total

memoria = mostrar_ram()
print(memoria)