class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def mostrar(self):
        print(f"Nombre Empresa: {self.nombre}")
        print("Empleados:")
        for empleado in self.empleados:
            empleado.mostrar()
        print("Clientes:")
        for cliente in self.clientes:
            cliente.mostrar()
