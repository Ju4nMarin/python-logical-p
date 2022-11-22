vocales = 0
consonantes = 0

#Sin condiciones de type

print("How many lines will there be?")
lineas = input()

for i in range (0, int(lineas)):
    print ("Line","(",i,")")
    palabra = input()
    for letra in palabra:
        if letra in ('aeiouAEIOU'):
            vocales += 1
        elif letra in ('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
            consonantes += 1


    
print("Number of vowels: " + str(vocales))
print("Number of consonants: " + str(consonantes))