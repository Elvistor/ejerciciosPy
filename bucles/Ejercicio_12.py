"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase."""

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
if letra in frase:
    print(f"La letra que ingresó se encuentra {frase.count(letra)} veces en su frase")