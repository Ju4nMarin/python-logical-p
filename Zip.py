

lista_nombres = ["Ana","Maria","Camilo","Javier"]
lista_edades = [23,45,34,63]

datos_zip = zip(lista_nombres, lista_edades)
print(list(datos_zip))

for nombre, edad in zip(lista_nombres, lista_edades):
    print(nombre, edad)