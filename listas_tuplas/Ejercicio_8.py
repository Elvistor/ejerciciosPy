"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

palabra = input("Ingrese una palagra: ")
if palabra.lower() == palabra[::-1].lower():
    print("Es un palíndromo")
else:
    print("No es un palíndromo")