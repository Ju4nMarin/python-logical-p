

lista_nombres = ["Ana","Maria","Camilo","Javier"]
lista_edades = [23,45,34,63]

datos_zip = list(zip(lista_nombres, lista_edades))
print(datos_zip)

Nombres_unzip, Edad_unzip = zip(*datos_zip)
print(Nombres_unzip)
print(Edad_unzip)

for nombre, edad in zip(lista_nombres, lista_edades):
    print(nombre, edad)