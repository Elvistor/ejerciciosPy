"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

precio = float(input("Ingrese el precio (máximo dos decimales): "))
decimal = (precio - int(precio)) * 100
entero = int(precio - decimal)
print(f"La parte entera es {entero}, y la parte decimal es {decimal: .2f}")