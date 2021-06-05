"""Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados."""

def cuadradosLista(lista):
    """Recibe como parámetro una lista y devuelve el cuadrado de sus elementos"""
    cuadradosLista = []
    for num in lista:
        cuadradosLista.append(num**2)
    return cuadradosLista

print(cuadradosLista([2,5,8,9,2,4]))