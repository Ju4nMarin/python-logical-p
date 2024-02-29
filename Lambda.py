

def separador(*args):
    par=[]
    impar=[]
    for numeros in args:
        if numeros %2 == 0:
            par.append(numeros)
        else:
            impar.append(numeros)  
    return par,impar          

print(separador(1,2,3,4,5,6,7,8,8,9))



lista_numeros = [1,2,3,4,5,6,7,8,8,9]
lista_pares = list(filter(lambda num: num %2 == 0,lista_numeros))
print(lista_pares)

multix2 = list(map(lambda lado: lado*2,lista_numeros))
print(multix2)
