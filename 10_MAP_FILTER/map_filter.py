# se usa para filtrar y tranformar
# diferente a listas de comprension
# es otra manera
# pero si o si toca primero tranformar y luego filtrar
# usa lambda la hp

usuarios = [
    ["chancho", 4],
    ["oscar", 1],
    ["pulga", 5]
]

# tranforrmando
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(f"trafnormando {nombres}")

# filtrando
menosUsuarios = list(filter(lambda usuario: usuario[1] > 1, usuarios))
print(f"filtrando {menosUsuarios}")
