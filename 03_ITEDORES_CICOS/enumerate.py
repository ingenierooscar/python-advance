#se usa para generar una tumpla enumareda apartir de una lista
"""
enumerate(iterable, start=0)
"""
nombres = ["hugo", "paco", "luis", "perra"] 
nombres_enumerados = enumerate(nombres)

for indice, elemento in enumerate(nombres):
    print(indice, elemento)

#lo mismo pero aumentando el indice
nombres_enumerados = enumerate(nombres, start = 5)
print(list(nombres_enumerados))