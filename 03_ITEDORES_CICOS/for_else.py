nombres = ["hugo", "paco", "luis", "perra"]

for nombre in nombres:
    print(nombre)
else:
    print("ya no hay mas putos nombres")

#romper el ciclo para que no use el else
for nombre_1 in nombres:
    print(nombre_1)
    if nombre_1 == "luis":
        break
else:
    print("no va a imprimir un culo porque el if no lo deja")
