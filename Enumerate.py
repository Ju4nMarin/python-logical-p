
nom = ["maria", "carlos", "julian", "yesica"]
num_nom = enumerate(nom, start= 5)
print(list(num_nom))

for indice, elemento in enumerate(nom):
    print(indice,elemento)
else:
    print("Finish...")