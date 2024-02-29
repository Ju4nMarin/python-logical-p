nom = ["samuel","camilo","karen"]

for elemento in nom:
    if elemento == "camilo":
        continue
    print(elemento)

for elemento in nom:
    if elemento == "camilo":
        break
    print(elemento)
