import os
import json
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def cargar_datos():
    try:
        with open("vehiculos.json", "r") as archivo:
            return json.load(archivo)
    except:
        return {}

def guardar_datos():
    with open("vehiculos.json","w") as archivo:
        json.dump(vehiculos,archivo, indent=4)
    return
def mostrar_menu():
    print("Menu Principal".center(50," "))
    print("-"*50)
    print("1 para ingresar un vehiculo ")
    print("2 para retirar un vehiculo ")
    print("3 registrar estado")
    print("4 listar vehiculos ")
    print("5 para salir ")
    opcion=input("ingrese una opcion: ")
    return opcion
def ingresar_vehiculo():
    print("ingresar vehiculo")
    patente=input("ingrese la patente: ")
    interior=input("Limpieza interior s/n: ")
    chasis=input("lavado de chasis s/n: ")
    motor=input("lavado de motor s/n: ")
    estado="pendiente"
    dniPropietario=input("ingrese el dni del propietario: ")
    vehiculos[patente]={
        "interior": interior,
        "chasis": chasis,
        "motor":motor,
        "estado":estado,
        "dniPropietario":dniPropietario
    } 
    guardar_datos()
    return
def retirar_vehiculo():
    return
def registrar_estado():
    print("menu cambio de estados")
    patente=input("ingrese la patente del vehiculo: ")
    if patente in vehiculos:
        vehiculo=vehiculos[patente]
        estado=input("ingrese el estado proceso/terminado/entregado")
        vehiculo["estado"]=estado
        guardar_datos()
    else:
        print("vehicolo no registrado!")
    return
def listar_vehiculos():
    print("listados")
    print("1 listar todos")
    print("2 listar pendientes ")
    print("3 listar en proceso ")
    print("4 listar terminados ")
    print("5 listar entregados ")
    print("6 menu anterior ")
    opcion=input("ingrese la opcion: ")
    if opcion=="1":
        for patente, vehiculo in vehiculos.items():
            print("patente: ", patente)
            print("interior: ",vehiculo["interior"] )
            print("chasis: ",vehiculo["chasis"] )
            print("motor: ",vehiculo["motor"] )
            print("estado: ",vehiculo["estado"] )
            print("dni: ",vehiculo["dniPropietario"] )
        input("presione enter para continuar")
    elif opcion=="2":
        print("listado de vehiculos pendientes")
        for patente, vehiculo in vehiculos.items():
            if vehiculo["estado"]=="pendiente":
                print("patente: ", patente)
                print("interior: ",vehiculo["interior"] )
                print("chasis: ",vehiculo["chasis"] )
                print("motor: ",vehiculo["motor"] )
                print("estado: ",vehiculo["estado"] )
                print("dni: ",vehiculo["dniPropietario"] )
        input("presione enter para continuar")

    return
def main():
    cargar_datos()
    while True:
        limpiar_pantalla()
        opcion =  mostrar_menu()
        if opcion == "1":
            ingresar_vehiculo()
        elif opcion == "2":
            retirar_vehiculo()
        elif opcion == "3":
            registrar_estado()
        elif opcion == "4":
            listar_vehiculos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")
    return
limpiar_pantalla()
#creo el diccionario de vehiculos
vehiculos = cargar_datos()
main()