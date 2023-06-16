piroos = [
    ["puta", 4],
    ["perra", 1],
    ["culo", 5]
]

#los map y filter es un alternativa a listas de comprension 
#no se pueden usar en una misma linea toca map y filter por separado


groserias = list(map(lambda groseria: groseria[0], piroos))
print(f"esto es con map {groserias}")

menosGroserias = list(filter(lambda groseria: groseria[1] > 2, piroos))
print(menosGroserias)

#siempre hay que decidir cual usar si filter, map o las listas de comprension
#usar las dos no es bueno es mala practica
#los que les gusta la progamacion funcional prefieren map y filter