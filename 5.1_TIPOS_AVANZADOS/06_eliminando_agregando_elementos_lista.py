groserias = ["gonorrea", "piroo", "hp", "perra", "hp"]

groserias.insert(0, "puta")
print(groserias)

#para agragar al final de la lista usar append
groserias.append("sapo")
print(groserias)

#para eleminar se usa remove
groserias.remove("hp")
print(groserias)

#para eliminar el ultimo se usa pop
groserias.pop()
print(groserias)

#eleminar elemnto en particular pop(2)
groserias.pop(-1)
print(groserias)

#otra forma de eleminar con del 
del groserias[1]
print(groserias)

#limpiar completamente el arreglo
groserias.clear()
print(groserias)
