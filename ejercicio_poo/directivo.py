from empleado import Empleado

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
    
    def mostrar(self):
        super().mostrar()
        print(f"Categoría: {self.categoria}")
