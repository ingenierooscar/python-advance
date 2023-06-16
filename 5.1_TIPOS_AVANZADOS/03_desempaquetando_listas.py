numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#asi se puede hacer pero se ve muy feo ese hp
#primero = numeros[0]
#segundo = numeros[1]
#tercero = numeros[2]

#primero, segundo, tercero = numeros
#print(segundo)

#para sacar un valor en particular
primer, *otros = numeros
print(primer, otros)
#para sacar el primero y el ultimo
primero, *otros, ultimo = numeros
print(primero, ultimo)