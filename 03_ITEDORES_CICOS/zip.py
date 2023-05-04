#los zip son para crear tupla con dos elementos de entrada o para crear dos tuplas apartir de un elemento de entrada

nombres = ["hugo", "paco", "luis", "perra"] #perra no se va a usar porque sobra con el apellido
apellidos = ["rico", "sabroso", "again"]

nombres_completo = list(zip(nombres, apellidos))
print(nombres_completo)

nombres_unzip, apellidos_unzip = zip(*nombres_completo)
print(nombres_unzip)
print(apellidos_unzip)

#usando for para recorrer dos elementos al timpo
for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)



