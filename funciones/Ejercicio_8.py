"""Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica."""

from math import sqrt

def med_var_es(lista):
    """Recibe como parámetro una lista, y devuelve en un diccionario su media, varianza y desviación típica"""
    #Definimos el diccionario
    diccionario = {}

    #Obtenemos media, la suma de los elementos de la lista, todo eso dividido por la cantidad de elementos.
    sum = 0
    for numero in lista:
        #Sumamos cada número
        sum += numero
        #A la suma de números se les divide por la cantidad de elementos de la lista
        media = sum/(len(lista))
    diccionario['media'] = media
    
    #Obtenemos varianza, la suma de las diferencias entre cada elemento de la lista y la media, todo eso dividido por la cantidad de elementos.
    diferenciaCuadrado = 0
    for num in lista:
        diferenciaCuadrado += (num - media)**2
    diccionario['varianza'] = diferenciaCuadrado/len(lista)

    #OLa desviación típica es igual a la raíz cuadrada de la varianza
    diccionario['desv_tipica'] = sqrt(diccionario['varianza'])

    return diccionario


print(med_var_es([4,5,6,7,8,9,1,3,5,4,8,9,6,5]))


        