priroos = [
    ["puta", 4],
    ["perra", 1],
    ["culo", 5]
]

#lo que queremos haces es pasar de una lista de usuarios a una lista de nombres
#solo los nombres

#haciendolo con for
nombres = []

for nombre in priroos:
    nombres.append(nombre[0])
print(f"este es con for {nombres}")    

#hay otra fomra de hacerlo mas elegante y en una sola hp linea
#lo que se usa es comprension de listas

#esto es tranformar osea map
groserias = [priroo[0] for priroo in priroos]
print(f"este es con list comprehensions tranformar osea map {groserias}")

#esto es filtar osea filter
groserias = [priroo for priroo in priroos if priroo[1] > 2]
print(f"este es filtrar con if {groserias}")

#esto es tranformar y filtrar map y filter
groserias = [piroo[0] for piroo in priroos if piroo[1] > 2]
print(f"estes es ambos filtar y tranformar {groserias}")