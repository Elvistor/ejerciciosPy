"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""
producto = input("Ingrese los productos separados por coma: ")
lista = producto.split(",")
for palabra in lista:
    print(palabra)
