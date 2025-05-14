# cliente.py
class Cliente:
    def __init__(self, nombre, clave, correo="", direccion=""):
        self.nombre = nombre
        self.clave = clave
        self.correo = correo
        self.direccion = direccion

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def to_dict(self):
        return {
            "clave": self.clave,
            "correo": self.correo,
            "direccion": self.direccion
        }

    @classmethod
    def from_dict(cls, nombre, data):
        return cls(nombre, data["clave"], data.get("correo", ""), data.get("direccion", ""))

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion}"
