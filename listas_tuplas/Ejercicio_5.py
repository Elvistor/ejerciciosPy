"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
pantalla en orden inverso separados por comas."""

lista_numeros = list(range(1,11))
print(sorted(lista_numeros, reverse=True))