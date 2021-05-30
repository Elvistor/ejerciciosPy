"""Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en 
una lista y muestre por pantalla su media y desviación típica."""

numeros = input("Ingrese una lista de 10 números separados por coma: ")
numeros = numeros.split(",")
media = 0
dif_cuadrado = 0
for numero in numeros:
    media += int(numero)
media /=len(numeros)
for numero in numeros:
    dif_cuadrado += (int(numero)-media)**2
varianza = dif_cuadrado/len(numeros)
print(f"Varianza: {varianza: .2f}")

print(f"Media: {media: .2f}")
