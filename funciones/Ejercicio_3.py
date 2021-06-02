"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""

def factorial(numero):
    factor = 1
    for num in range(1,numero+1):
        factor = factor*num
    return factor

