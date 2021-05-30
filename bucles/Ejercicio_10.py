"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número 
primo o no."""

entero = int(input("Ingrese un número: "))
divisor = []
for num in range(2,entero):
    if entero%num == 0:
        divisor.append(num)
if len(divisor) == 0:
    print("Es Número primo")
else:
    print("No es Número primo")

