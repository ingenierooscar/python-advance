def calcular_cuadrado(numero):
    return numero**2

lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []

"""
esto es usando un for para hacer recorrido y pasarlos a una funcion
para despues imprimirlos o capturarlos

for num in lista_numero:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)"""

map_cuadrados = list(map(calcular_cuadrado, lista_numero))
print(map_cuadrados)

#los maps se usa para a una funcion pasarle parametros
