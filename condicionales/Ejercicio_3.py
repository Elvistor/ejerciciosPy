"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error."""
try:
    numero_1 = float(input("Ingrese un número (dividendo): "))
    numero_2 = float(input("Ingrese un número (divisor): "))
except ValueError:
    print("No hay ingresado un número")

try:
    resultado = numero_1/numero_2
except ZeroDivisionError:
    print("No se puede dividir por cero.")