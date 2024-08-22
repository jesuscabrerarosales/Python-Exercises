class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        if isinstance(other, Persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

    def __add__(self, other):
        if isinstance(other, Persona):
            nuevo_nombre = self.nombre + " " + other.nombre
            nueva_edad = self.edad + other.edad
            return Persona(nuevo_nombre, nueva_edad)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Persona):
            nuevo_nombre = self.nombre
            nueva_edad = self.edad * other.edad
            return Persona(nuevo_nombre, nueva_edad)
        return NotImplemented

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


# Ejemplo de uso
persona1 = Persona("Juan", 30)
persona2 = Persona("Job", 20)
# persona3 = Persona("Ana", 25)

# Sobrecarga de ==
print(persona1 == persona2)  # True
print(persona2 == persona1)  # False

# Sobrecarga de +
persona_sumada = persona1 + persona2
print(persona_sumada)  # Nombre: Juan Ana, Edad: 55

# Sobrecarga de *
persona_multiplicada = persona1 * persona2
print(persona_multiplicada)  # Nombre: Juan, Edad: 750
