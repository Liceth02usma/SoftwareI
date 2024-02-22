import os

class Archivo:
    def __init__(self, path_archive):
        self.path = path_archive
        self.number_words = 0

    def contar_palabra(self, word):
        try:
            with open(self.path, 'r') as archivo:
                contenido = archivo.read()
                # Reemplazar caracteres no alfabéticos con espacios para asegurar la correcta cuenta de la palabra
                contenido_alfab = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in contenido)
                # Contar la cantidad de veces que aparece la palabra en el contenido del archivo
                self.number_words = contenido_alfab.lower().split().count(word.lower())
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.path}")

    def __str__(self):
        return f'En el archivo {os.path.basename(self.path)} la palabra aparece {self.number_words} veces'

class Carpeta:
    def __init__(self, path):
        self.path = path
        self.archivos = []

    def create_archive(self):
        try:
            archivos_en_carpeta = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        except FileNotFoundError:
            print(f"No se encuentra la carpeta: {self.path}")
            return

        for name in archivos_en_carpeta:
            if name.lower().endswith(('.txt', '.xml', '.json', '.csv')):
                archivo = Archivo(os.path.join(self.path, name))
                self.archivos.append(archivo)

    def contar_palabra_en_archivos(self, word):
        if not self.archivos:
            print(f"No se encontraron archivos de texto en la carpeta {self.path}")
            return

        total_palabras_en_carpeta = 0
        for archivo in self.archivos:
            archivo.contar_palabra(word)
            total_palabras_en_carpeta += archivo.number_words
            print(archivo)

        print(f'\nTotal de veces que la palabra aparece en la carpeta: {total_palabras_en_carpeta}')

# Pedir nombre y path de la carpeta
path_carpeta = input("Ingrese la ruta de la carpeta: ")

# Crear objeto Carpeta
carpeta = Carpeta(path_carpeta)

# Crear archivos en la carpeta
carpeta.create_archive()

# Ingresar la palabra a buscar
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

# Contar palabras en los archivos
carpeta.contar_palabra_en_archivos(palabra_a_buscar)




