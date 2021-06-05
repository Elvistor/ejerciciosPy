"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."""

from math import pi, sqrt

def areaCirculo(radio):
    """Recibe como parámetro el radio de un círculo y calcula el área de un círculo"""
    #Fórmula de cálculo del área de cun círculo
    area = pi*radio**2
    return area

def areaCilindro(areaCirculo, altura):
   """Recibe el área de un círculo y la altura, devuelve el área de un cilindro (2πr2 + 2πrh)"""
   #Obtenemos el radio del área
   rad = sqrt(areaCirculo/pi)
   cilindro = (2*areaCirculo) + (2*pi*rad*altura)
   return cilindro

print(f'{areaCilindro(areaCirculo(5),2): .2f}')