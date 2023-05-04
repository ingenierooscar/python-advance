#kwargs son parametros tipo diccionario
def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])

funcion_kwargs = funcion_kwargs(nombre="paco", apellido="Botero")