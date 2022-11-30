lista_num = [1, 3, 5, 1, 3, 2, 8, 7, 6]

set_pares = {num for num in lista_num if num % 2 ==0}
print(set_pares)

vocales = "aeiou"

diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)