lista_app = [1,2,3]
lista_ext = [4,5,6]
lista_ins = [7,8,9]

lista_letras = ["a","b","c"]

lista_app.append(lista_letras)
print(lista_app)

lista_ext.extend(lista_letras)
print(lista_ext)

lista_ins.insert(1,lista_letras)
print(lista_ins)