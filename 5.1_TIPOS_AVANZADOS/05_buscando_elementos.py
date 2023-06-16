groserias = ["gonorrea", "piroo", "hp", "perra", "hp"]

#busca con index y le dice el indice donde se ubica
print(groserias.index("hp"))

#para que no salga error primero valida si existe el elemento
if "perra" in groserias:
    print(groserias.index("perra"))

#validar si hay errores repetidos
print(groserias.count("hp"))    