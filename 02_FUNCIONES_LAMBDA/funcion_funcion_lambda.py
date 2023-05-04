def serparar_par_impar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def calcular_area_cuadrado(lado):
    return lado ** 2

#para hacer expresiones lambda es necesario que sean sencillas
#ejemplo la funcion calcular area cuadrado si se puede hacer mientras la otra no

calcular_cuadrado = lambda lado: lado ** 2
print(calcular_cuadrado(2))

#muchos dicen que es mejor evitarlas
#pero para lo que mas se usa es los filters y map