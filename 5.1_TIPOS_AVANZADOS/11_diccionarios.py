#los diccionarios tienen una llave que es string y el valor cualquiera
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

#agregar
punto["z"] = 45

#validar si existe la llave
if "lala" in punto:
    print("bobo marica si hat lala", punto["lala"])

#acceder a valores por medio de get
print(punto.get("z"))
#como no existe lala lo va a agregar por get
print(punto.get("lala", 97))

#eliminar
del punto["x"]
del punto["y"]
print(punto)

punto["x"] = 25

#acceder a las llaves
for llaves in punto:
    print(llaves)

#acceder a los valores
for valor in punto:
    print(valor, punto[valor])

#haciendo eso mismo pero mejor y genera una tupla
for valor in punto.items():
    print(valor)

#desempaquetando
for llave, valor  in punto.items():
    print(llave ,valor)

#un puto ejemplo real
usuarios = [
    {"id": 1, "nombre": "bobo"},
    {"id": 2, "nombre": "hp"},
    {"id": 3, "nombre": "malparida"},
    {"id": 4, "nombre": "perra"}
]

for usuario in usuarios:
    print(usuario["nombre"])