"""Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

def media(lista):
    """Recibe como parámetro una lista de números y devuelve la media"""
    sum = 0
    #Recorremos la lista
    for numero in lista:
        #Sumamos cada número
        sum += numero
        #A la suma de números se les divide por la cantidad de elementos de la lista
        media = sum/(len(lista))
    return media


print(media([1,2,3,4,10,6,7,8,9]))