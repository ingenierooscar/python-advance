from ast import arg


def calcular_perimetro(lado_1, lado_2, lado_3, lado_4):
    perimetro = lado_1 + lado_2 + lado_3 + lado_4
    return perimetro

perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)

#hacer lo mismo pero con un for y con *args, args es una tupla

def calcular_parametro_args(*args):
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro = calcular_parametro_args(1,2,3,4)
print(perimetro)

triangulo = calcular_parametro_args(1,2,3)
print(triangulo)