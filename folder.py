import os

def lista_archivos(ruta):
    lista_archivos = os.listdir(ruta)
    return lista_archivos

ruta_absoluta = os.getcwd()
ruta_relativa = "folder/"
archivos = lista_archivos(ruta_absoluta)
print(archivos)