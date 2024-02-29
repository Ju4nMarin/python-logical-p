def square(num):
    return num**2

def par(num):
    return num %2 == 0

lista_num = list(range(1,11))
lista_square = []

"""
for element in lista_num:
    square_num = square(element)
    lista_square.append(square_num)

print(lista_square)    
"""

map_square = list(map(square,lista_num))
print(map_square)

lista_comprehension = [square(num) for num in lista_num]
print(lista_comprehension)

lista_comprehension_par = [square(num) for num in lista_num if par(num)]
print(lista_comprehension_par)

lista_comprehension_par2 = [square(num) if par(num) else 0 for num in lista_num]
print(lista_comprehension_par2)

set_par = {num for num in lista_num}
print(set_par)

vocales = "aeiou"
dicccionario = {vocal.lower(): vocal.upper() for vocal in vocales }
print(dicccionario)
