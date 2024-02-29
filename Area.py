def area(lado):
    """Calcular el are de un cuadrado"""
    area = lado * lado
    return area

area_cuadrado = area(lado=5)
print(area_cuadrado)


def perimetro(*args):
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

per = perimetro(1,2,3,4)
print(per)

def funcion_kwargs(**kwargs):
    print(1,kwargs)
    for llave, valor in kwargs.items():
        print(2,f"LLave: {llave}, valor: {valor}")
    print(3,kwargs["nombre"],kwargs["apellido"])

funcion_kwargs(nombre="Paco", apellido="Marin")    


