"""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""

frase = input("Introduzca la frase: ")
vocal = input("Introduzca una vocal: ")
print(frase.replace(vocal.lower(), vocal.upper()))
