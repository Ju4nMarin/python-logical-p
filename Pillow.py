import os
from PIL import Image


def abrir(ruta_img):
    imagen = Image.open(ruta_img)
    imagen.show()


ruta_relativa = "pintura.png"
ruta_absoluta = os.path.join(os.getcwd(), ruta_relativa)

abrir(ruta_absoluta)