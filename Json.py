import json

persona = {
    "nombre": "Javier",
    "edad": 12,
   
}

objecto_json = json.dumps(persona,indent=2)
print(objecto_json)
with open("persona.json","w") as archivo_json:
    archivo_json.write(objecto_json)

with open("persona.json","r") as archivo_json:
    datos_json = json.load(archivo_json)

print(datos_json)
   