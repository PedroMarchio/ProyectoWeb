# main.py
import json
import os
from cliente import Cliente

BDD_File = 'usuarios.json'

clientes = {}

if os.path.exists(BDD_File) and os.stat(BDD_File).st_size > 0:
    with open(BDD_File, 'r', encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for nombre, info in datos.items():
            clientes[nombre] = Cliente.from_dict(nombre, info)

def guardar_datos():
    with open(BDD_File, 'w', encoding='utf-8') as archivo:
        datos = {nombre: cliente.to_dict() for nombre, cliente in clientes.items()}
        json.dump(datos, archivo, indent=2)

def registrarUsuario():
    nombre = input(str("""---------------------------------------
REGISTRATE:

  Ingrese un usuario: """))
    clave = input(str("  Ingrese una clave: "))
    correo = input(str("  Ingrese un correo: "))
    direccion = input(str("  Ingrese una dirección: "))

    nuevo_cliente = Cliente(nombre, clave, correo, direccion)
    clientes[nombre] = nuevo_cliente
    guardar_datos()

    print("""-----------------------------------------
  Usuario crado exitosamente""")

def verUsuarioBD():
    print("""-----------------------------------------
  La Base de Datos de Usuario contiene:
  """)
    for cliente in clientes.values():
        print(cliente)

def Login():
    nombre = input("Ingresa tu usuario: ")
    clave = input("Ingresa tu clave: ")
    cliente = clientes.get(nombre)
    if cliente and cliente.clave == clave:
        print(f"Hola {cliente.nombre}! ¡A trabajar!")
        return 1
    else:
        print("Usuario o clave incorrectos.")
        return 0

# Menú principal
opcionMenu = 0
while opcionMenu == 0:
    try:
        opcionUsuario = int(input("""-----------------------------------------

    Hola ¿Que quieres hacer?

    1-Logearme.
    2-Registrarme.
    3-Ver base de datos de usuarios.
    4-Salir del prgrama.

-----------------------------------------
>"""))
    except:
        print("""-----------------------------------------
        Las opciones correctas son 1, 2, 3 y 4; vuelve a intentarlo""")
        continue
    if opcionUsuario == 1:
        opcionMenu = Login()
    elif opcionUsuario == 2:
        registrarUsuario()
    elif opcionUsuario == 3:
        verUsuarioBD()
    elif opcionUsuario == 4:
        opcionMenu = 1
    else:
        print("""-----------------------------------------
        Las opciones correctas son 1, 2, 3 y 4; vuelve a intentarlo""")

print("Programa terminado.")
