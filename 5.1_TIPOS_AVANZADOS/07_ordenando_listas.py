numeros = [2, 5, 6, 8, 7, 9, 3, 1]

#otra forma de ordenar es con sorted pero devulve una lista
numeros2 = sorted(numeros)
print(numeros2)

#igual pero al reves 
numeros3 = sorted(numeros, reverse=True)
print(numeros3)

#para ordenar sort
numeros.sort()
print(numeros)

#para ordenar pero alreves 
numeros.sort(reverse=True)
print(numeros)

#hacer algo mas complejo
priroos = [
    ["puta", 4],
    ["perra", 1],
    ["culo", 5]
]

def ordena(elemento):
    return elemento[1]

priroos.sort(key=ordena)
print(priroos)