lista_numeros = [1,2,3,4,5,6,7,8,9]

#con esta funcion lambda podeos crear filtros
lista_pares = list(filter(lambda numero : numero %2 == 0, lista_numeros))
print(lista_pares)

#este es otro caso de uso map que recibe unos datos y con una funcion lambda los procesa
nueva_lista = list(map(lambda numeros : numeros*10, lista_numeros))
print(nueva_lista)

#las expresiones lambda no se deben usar repetidas veces ni mucho porque son dificiles de leer