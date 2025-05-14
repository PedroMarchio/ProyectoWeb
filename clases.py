class Cliente:
    id = 0

    def __init__(self, nombre, correo, clave, edad):
        self.nombre = nombre
        self.correo = correo
        self.clave = clave
        self.edad = edad
        self.id += 1
    
    def __str__(self):
        return f"""Cliente {self.id}: {self.nombre}\nSe creo con exito"""
    
    def verClave(self):
        return self.clave

cliente1 = Cliente("Pedro", "pedro@gmail.com", "123456", "30")

print(cliente1)

print(cliente1.verClave())