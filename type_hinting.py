from typing import Union

def perimetro(lado: Union[int,float]) -> Union[int,float]:
    return 4* lado

print(perimetro(lado=5.1))