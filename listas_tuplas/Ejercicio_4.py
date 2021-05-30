"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

numeros = []
while input("Desea agregar un número? (s/n): ") == "s":
    numeros.append(int(input("Número: ")))
else:
    print(sorted(numeros))