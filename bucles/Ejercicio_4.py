"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
cuenta atrás desde ese número hasta cero separados por comas."""
lista = []
numero = int(input("Ingrese un númeo entero positivo: "))
for i in range(numero):
    lista.append(i)
print(lista[::-1])