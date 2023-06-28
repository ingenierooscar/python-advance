pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimoElemento = pila.pop()
print(ultimoElemento)

print(pila)
print(pila[-1])

pila.clear()

if not pila:
    print("pila vacia")

#este son los lifo (last in, first out)