from empresa import Empresa
from empleado import Empleado
from directivo import Directivo
from cliente import Cliente

# Crear instancias de Empresa, Empleado, Directivo y Cliente
empresa = Empresa("Tech Corp")
empleado = Empleado("Juan", 30, 2000)
directivo = Directivo("Ana", 40, 5000, "Gerente")
cliente = Cliente("Carlos", 35, "Client S.A.", "123-456-789")

# Agregar empleados y clientes a la empresa
empresa.agregar_empleado(empleado)
empresa.agregar_empleado(directivo)
empresa.agregar_cliente(cliente)

# Mostrar los detalles de la empresa
empresa.mostrar()
