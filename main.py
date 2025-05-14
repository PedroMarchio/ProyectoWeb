import json
import os

# Lectura y deserialización desde un archivo JSON
BDD_File = 'usuario.json'

if os.stat(BDD_File).st_size == 0:
    usuarioBD = {}
else:
    with open(BDD_File, 'r', encoding="utf-8") as archivo:
        usuarioBD = json.load(archivo)

print(usuarioBD)

#usuarioBD = {"administrador":123456}
opcionMenu = 0

def registrarUsuario():
  usuario = input(str("""-----------------------------------------
REGISTRATE:

  Ingrese un usuario: """))
  clave = input(str("  Ingrese una clave: "))
  
  usuarioBD[usuario] = clave

  with open(BDD_File, 'w', encoding='utf-8') as archivo:
    json.dump(usuarioBD, archivo, indent=2)

  print("""-----------------------------------------
  Usuario crado exitosamente""")

def verUsuarioBD():
  print("""-----------------------------------------
  La Base de Datos de Usuario contiene:
  """)
  for x in usuarioBD:
    print(f"- Usuario: {x} Clave: {usuarioBD[x]}")
  print("""
  Volver al inicio""")

def Login():
  usuario = input(str("""-----------------------------------------
INGRESÁ:

  Ingresa tu usuario: """))
  clave = input(str("  Ingrese tu clave: "))
  try:
    if usuarioBD[f"{usuario}"] == clave:
      print(f"""-----------------------------------------
    ¡Hola {usuario}! ¡A TRABAJAR QUE ACA NO SE LE REGALA EL SUELDO A NADIE! (Ahora el programa finaliza podria hacr otra cosa distinta)""")
    return 1
  except KeyError:
    print("""-----------------------------------------
    La clave o el usuario son incorectos... volviendo al menu inicial""")
  return 0



while opcionMenu == 0:
  try:
    opcionUsuario = int(input("""-----------------------------------------

    Hola ¿Que quieres hacer?

    1-Logearme.
    2-Registrarme.
    3-Ver base de datos de usuarios.
    4-Salir del prgrama.

-----------------------------------------
"""))
  except:
    print("""-----------------------------------------
    Las opciones correctas son 1, 2, 3 y 4; vuelve a intentarlo""")
    continue
  if opcionUsuario == 1:
    opcionMenu = Login()
  elif opcionUsuario ==2:
    registrarUsuario()
  elif opcionUsuario ==3:
    verUsuarioBD()
  elif opcionUsuario ==4:
    opcionMenu=1
  else:
    print("""-----------------------------------------
    Las opciones correctas son 1, 2, 3 y 4; vuelve a intentarlo""")

print("""-----------------------------------------
Programa termindo""")