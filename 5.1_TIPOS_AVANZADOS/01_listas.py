#listas son del grupo de tipos avanzados en python

#las listas se usan con corchetes [], tambien se usa para acceder a los indices de un string
print("oscar rodiguez"[3:])

numeros = [1,2,3]
print(numeros)

letras = ["a", "b", "c"]
palabras = ["gonorrea", "piroo", "hp"]
booleanos = [True, False]
matriz = [[0,1], [2,2]]

#listado con 10 ceros
ceros = [0] * 10
#juntar listas
alfanumrico = numeros + letras
print(alfanumrico) 

#usando la funcion rango
print(list(range(1,11)))

chars = list("holaGonorrea")
print(chars)