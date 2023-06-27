numeros = [1, 2, 3, 4]
print(*numeros)

numeros2 = (5,6)
print(*numeros2)

cominada = ["hola", *numeros, *numeros2, "hp"]
print(cominada)

#tambien con diccionarios
punto1 = {"x": 15}
punto2 = {"y": 20}

nuevoPunto = {**punto1, **punto2, "mira": "bobo hp"}
print(nuevoPunto)