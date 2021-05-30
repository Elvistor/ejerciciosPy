"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""
try:
    numero = int(input("Ingrese un número entero: "))
except ValueError:
    print("No es un número entero")
if numero % 2 == 0:
    print("es par")
else:
    print("es impar")
