import matplotlib.pyplot as plt

# Datos
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
ventas = [50, 75, 30, 90]

# Gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(productos, ventas, color=['red', 'blue', 'green', 'purple'])
plt.xlabel('Productos')
plt.ylabel('Ventas')
plt.title('Ventas por Producto')
plt.show()

# Gráfico de pastel
plt.figure(figsize=(7, 7))
plt.pie(ventas, labels=productos, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'purple'])
plt.title('Proporción de Ventas por Producto')
plt.show()
