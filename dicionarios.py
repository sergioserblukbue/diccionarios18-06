
personas=[]
datosPersona = {
    "nombre": "Gustavo",
    "apellido": "Borini",
    "edad": 55,
    "telefono": 3471575990,
    "jubilado:": False,
    "hijos": ["Barbara", "Theo"]
}
personas.append(datosPersona)
datosPersona = {
    "nombre": "juan",
    "apellido": "perez",
    "edad": 55,
    "telefono": 3471575990,
    "jubilado:": False,
    "hijos": ["Barbara", "Theo"]
}
personas.append(datosPersona)

n="juan"
a="perez"
for i in range(len(personas)):
    if personas[i]["nombre"]==n and personas[i]["apellido"]==a:
        for c, v in personas[i].items():
            print(f"{c}: {v}")
        nom=input("ingrese el nuevo nombre: ")
        personas[i]["nombre"]= nom

print(personas)











