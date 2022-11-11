#este es de como usar las palabras resevadas en python de break y continuo para for

nombres = ["hugo", "paco", "luis"]
for elemento in nombres:
    if elemento == "paco":
        continue
    print(elemento)


nombres = ["hugo", "paco", "luis"]
for elemento in nombres:
    break
    print(elemento)
    
    