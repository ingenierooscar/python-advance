#las tuplas son lo mismo que las listas solo que los valores no se pueden modificar
#puedes crear nuevas tuplas o listas a base de otras tuplas 
#se usan ()

nuemros = (1, 2, 3) + (1, 2, 3) #concatenar
print(nuemros)

#pasar a una tupla
punto = tuple([1, 2])
print(punto)

#no se pueden usar los mismos metodos que las listas

#creando otras tuplas
menosNumeros = nuemros[:2]
print(menosNumeros)

primero, segundo, *otros = nuemros
print(primero, segundo, otros)

for n in nuemros:
    print(n)

listasNumeros = list(nuemros)
listasNumeros[0] = "perra"
print(listasNumeros)

#con las tuplas se supone que no debo cambiar nada pero si lo requiero lo paso a una lista y nuvamente a una tupla