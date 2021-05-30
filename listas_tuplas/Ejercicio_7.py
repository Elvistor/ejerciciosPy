"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""

abecedario = []
while True:
    letras = input("Letra: ")
    if letras == "salir":
        break
    else:
        abecedario.append(letras)

for i in range(len(abecedario)):
    if i > 0 and i%3 == 0:
        abecedario.pop(i)
print(abecedario)