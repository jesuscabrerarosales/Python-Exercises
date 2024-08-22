from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, edad, nombre_empresa, telefono_de_contacto):
        super().__init__(nombre, edad)
        self.nombre_empresa = nombre_empresa
        self.telefono_de_contacto = telefono_de_contacto
    
    def mostrar(self):
        super().mostrar()
        print(f"Nombre Empresa: {self.nombre_empresa}, Teléfono de Contacto: {self.telefono_de_contacto}")
