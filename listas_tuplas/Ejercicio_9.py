"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces
 que contiene cada vocal."""

vocales = ["a", "e", "i", "o", "u"]
contador = []
letras = []

palabra = input("Ingrese una palabra: ")
#Recorrer la palabra
for letra in range(len(palabra)):
    lista_temporal = []
    #Si la letra se encuentra en la lista de vocales.
    if palabra[letra] in vocales:
        #Si la lista contador está vacía, o la letra actual no se encuentra en la lista
        #de vocales agregadas
        if len(contador) == 0 or palabra[letra] not in letras:
            lista_temporal.append(palabra[letra])
            letras.append(palabra[letra])
            lista_temporal.append(palabra.count(palabra[letra]))
            contador.append(lista_temporal)
#Si la lista contador no se encuentra vacía, recorrer.
if len(contador) != 0:
    for vocal,cantidad in contador:
        if cantidad == 1:    
            print(f"La vocal {vocal} se repite {cantidad} vez.")
        else:
            print(f"La vocal {vocal} se repite {cantidad} veces.")
else:
    print("La lista está vacía.")
