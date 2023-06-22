#los sets son conjuntos
#podemos usar los metodos de insert, append, remove, pop
#tenemos otros operadores con ellos

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]

segundo = set(segundo)

#union
print(primer | segundo)

#interceccion
print(primer & segundo)

#diferencia
print(primer ^ segundo)

#validar si existe un elemento
if 5 in segundo:
    print("bobo marica obvio que si esta el 5")

primer.add(6)
print(primer)