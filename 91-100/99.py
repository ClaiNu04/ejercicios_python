


class Archivo:
    def __init__(self):
        self.nombre_archivo = ''
        self.contenido_archivo = ''

    def set_nombre_archivo(self, nombre):
        self.nombre_archivo = nombre

    def set_contenido_archivo(self, contenido):
        self.contenido_archivo = contenido

    def crear_archivo(self):
        with open(self.nombre_archivo, 'w'):
            pass

    def escribir_archivo(self):
        with open(self.nombre_archivo, 'w') as archivo:
            archivo.write(self.nombre_archivo)

    def leer_archivo(self):
        with open(self.nombre_archivo, 'r') as archivo:
            informacion = archivo.read()
        return informacion

file = Archivo()
file.set_nombre_archivo('archivo.txt')
file.set_contenido_archivo('Hola como estas, autodidacta?')
file.crear_archivo()
file.escribir_archivo()
print(file.leer_archivo())