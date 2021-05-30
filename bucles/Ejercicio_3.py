"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas."""
lista = []
numero = int(input("Ingrese un número entero positivo: "))
for num in range(numero):
    if num % 2 != 0:
        lista.append(num)
print(lista)