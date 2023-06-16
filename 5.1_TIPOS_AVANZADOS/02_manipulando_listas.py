groserias = ["gonorrea", "bobo", "hp", "culo"]
print(groserias[0])

#cambiar valores de una lista
groserias[0] = "malparido"
print(groserias)

#solo una parte parcial igual que los strings
print(groserias[-1:])
#para saltar de 2 en 2
print(groserias[1::2])

#devolver numeros impares
numeros = list(range(1,21))
print(numeros[::2])