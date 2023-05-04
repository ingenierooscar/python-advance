#son rangos que se pueden crear
# range(inicio, fin, paso)
#con list creamos una lista

serie_1 = range(5) #como no se puso nada lo toma como fin
print(list(serie_1))

serie_2 = range(5, 10) #como puse dos va de inicio a fin
print(list(serie_2))

serie_3 = range(3,10,2)#como le puse todo va de 3 a 10 de 2 en 2
print(list(serie_3))

#se podria hacer con for pero asi para recorrerlo
for elemento in serie_3:
    print(elemento)

