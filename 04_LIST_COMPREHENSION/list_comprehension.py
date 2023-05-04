#las list comprehension es una manera de construir listas o objetos iterables
#usando una linea de codigo

"""lista = [expresion(elemento) for elemento in objeto_iterable)]"""

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = num ** 2
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)

lista_comprehension = [num ** 2 for num in lista_num]
print("por comprehension", lista_comprehension)

#usando un metodo como expresion
def cuadrado(numero):
    return numero ** 2

lista_comprehension2 = [cuadrado(num) for num in lista_num]
print("usando una funcion", lista_comprehension2)

#es usar para hacer listas de forma breve papi
#primero la funcion o calculo, depues un for dondte itere una lista