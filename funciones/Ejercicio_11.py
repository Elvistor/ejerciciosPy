"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""

def palabrasRepetidas(frase):
    """Recibe como parámetro una cadena de caracteres y devuelve un diccionario con cada palabra que contiene y su frecuencia"""
    #Separamos cada palabra en la frase y eliminamos los repetidos
    conjunto = set(frase.split(' '))
    diccionario = {}
    #Recorremos el conjunto de palabras y asignamos la candidad en un diccionario
    for palabra in conjunto:
        diccionario[palabra] = frase.count(palabra)
    return diccionario


def max_palabrasRepetidas(diccionario):
    """Recibe como parámetro un diccionario y devuelve una tupla con la palabra mas repetida y su frecuencia"""
    lista = []
    #Recorremos cada elemento del diccionario
    for palabra, cantidad in diccionario.items():
        #Agregamos con formato de tuplas a una lista
        lista.append((palabra, cantidad))
        #Definimos a "t" como key para usarlo como referencia, y ordenamos de acuerdo a "t" en orden descendente
        lista = sorted(lista, key=lambda t: t[1], reverse = True)
    #Devolvemos el primer valor de la lista, corresponde al de mayor frecuencia
    return lista[0]


