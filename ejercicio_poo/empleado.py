from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto
    
    def calcular_salario_neto(self):
        return self.sueldo_bruto + (0.20 * self.sueldo_bruto)
    
    def mostrar(self):
        super().mostrar()
        print(f"Sueldo Bruto: {self.sueldo_bruto}, Sueldo Neto: {self.calcular_salario_neto()}")
