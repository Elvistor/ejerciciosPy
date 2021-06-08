"""Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo."""

#Máximo Común Divisor
def mcd(num1, num2):
    """Recibe como parámetro 2 números y devuelve el mínimo común divisor"""
    menor = 0
    #Comparamos cuál es el menor de ambos parámetros
    #Los divisores no deben ser mayor al parámetro de menor valor
    if num1 > num2:
        menor = num2
    else:
        menor = num1
    #Creamos una lista donde se van a almacenar los valores que cumplan la condición
    listaDivisores = []
    #Recorremos desde 1 hasta el menor
    for numero in range(1, menor):
        #Si el módulo de la división en ambos parámetro da cero, lo agregamos a lista
        if num1 % numero == 0 and num2 % numero == 0:
            listaDivisores.append(numero)
    #ODevolvemos el máximo valor de la lista
    return max(listaDivisores)


#Mínimo Común Múltiplo
def mcm(num1, num2):
    #Determinamos qué parámetro es el mayor y cuál el menor
    menor = 0
    mayor = 0
    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1
    #Definimos una lista donde se van a almacenar los múltiplos del mayor valor
    #Va a recorrer un rango de 2 a 1000 hasta que el múltiplo del parámetro de menor valor se encuentre en la lista, y devuelve el valor 
    multiplosMayores = []
    multiplo = 0
    for i in range(2,1000):
        multiplosMayores.append(mayor*i)
        multiplo = menor*i
        #Si el resultado del producto entre el menor valor e "i" se encuentra dentro de la lista de productos entre el mayor valor e "i", devuelve el valor de la variable múltiplo.
        if multiplo in multiplosMayores:
            return multiplo
    return False

