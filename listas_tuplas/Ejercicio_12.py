"""Escribir un programa que almacene las matrices
A = (1, 2, 3        B = (-1, 0
     4, 5, 6)             0, 1
                          1, 1)
        
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, 
representando cada vector fila en una lista."""
matriz_a = [
    [1,2,3],
    [4,5,6]
]
matriz_b = [
    [-1,0],
    [0,1],
    [1,1]
]

filas_a = len(matriz_a)
filas_b = len(matriz_b)
columnas_a = len(matriz_a[0])
columnas_b = len(matriz_b[0])
if columnas_a != filas_b:
    print("No se puede multiplicar")

# Generar los espacios en la nueva matriz
producto = []
for i in range(filas_a):
    producto.append([])
    for j in range(columnas_b):
        producto[i].append(None)
print(producto)

# Rellenar el producto
for c in range(columnas_b):
    for i in range(filas_a):
        suma = 0
        for j in range(columnas_a):
            suma += matriz_a[i][j]*matriz_b[j][c]
        producto[i][c] = suma
print(producto)

