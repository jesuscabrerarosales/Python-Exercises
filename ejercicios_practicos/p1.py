# Función para obtener números únicos del usuario
def obtener_numeros_unicos():
    numeros = set()  # Usamos un conjunto para evitar números repetidos
    while len(numeros) < 15:
        try:
            num = int(input("Introduce un número: "))
            if num in numeros:
                print("Número repetido. Intenta de nuevo.")
            else:
                numeros.add(num)
        except ValueError:
            print("Por favor, introduce un número válido.")
    return list(numeros)  # Convertimos el conjunto en lista

# Obtener los 15 números únicos del usuario
numeros = obtener_numeros_unicos()

# Utilizar lambda y list comprehension para calcular la suma de los cuadrados de los números pares
suma_cuadrados_pares = sum((lambda x: [i**2 for i in x if i % 2 == 0])(numeros))

print(f"La suma de los cuadrados de los números pares es: {suma_cuadrados_pares}")
