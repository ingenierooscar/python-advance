import json

persona = {
    "nomre": "bobo",
    "apellido": "marica",
    "edad": 100
}

#objeto_json = json.dumps(persona, indent=2)

with open("persona.json", "w") as archivo_json:
    #archivo_json.write(objeto_json)
    json.dump(persona, archivo_json)