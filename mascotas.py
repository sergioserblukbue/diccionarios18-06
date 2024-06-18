pacientes=[]
mascota={
    "nombre":"pepe",
    "tipo":"loro",
    "raza":"paraguayo",
    "dni":"2424"
}
pacientes.append(mascota)
mascota={
    "nombre":"pepe",
    "tipo":"reptil",
    "raza":"cururu",
    "dni":"2420"
}
pacientes.append(mascota)
mascota={
    "nombre":"capitan",
    "tipo":"perro",
    "raza":"labrador",
    "dni":"2420"
}
pacientes.append(mascota)
dni=input("ingrese el dni del dueño: ")
for m in pacientes:
    if m["dni"]==dni:
        print(f"mascota: {m['nombre']} dni dueño: {m['dni']}")