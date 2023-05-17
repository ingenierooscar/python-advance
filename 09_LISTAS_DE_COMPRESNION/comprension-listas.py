# list comprehension, comprension de listas
# es para crear una lista en base a otra lista

usuarios = [
    ["chancho", 4],
    ["oscar", 1],
    ["pulga", 5]
]

"""esto se hace pero es feo
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)
"""
# con comprension de listas creando nueva lista modificando la original
# in tranforma
nombres = [usuario[0] for usuario in usuarios]
print(f"con tranformacion de listas {nombres}")

# creando lista y filtrando
# if filtra
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(f"con filtro de listas {nombres}")

# filtrar y tranformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(f"filtrada y tranformada: {nombres}")
