"""Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal."""

def decimal_binario(numero):
    """Recibe como parámetro un valor menor a 1.024 y lo convierte a binario"""
    #Definimos la lista de valores equivalentes a las potencias con base 2
    lista = [512,256,128,64,32,16,8,4,2,1]
    #Definimos una lista con la misma cantidad de números que la lista anterior, donde se van a ir reemplazando por 1 en caso de cumplirse la condición
    lista_binario = ['0','0','0','0','0','0','0','0','0','0']
    #Será el string a ser devuelto por la función
    numero_binario = ''
    #Recorremos "lista"
    for posicion in range(len(lista)):
        #Comparamos cada elemento, si el parámetro ingresado es mayor o igual, le restamos al parámetro, el valor actual de la lista, y en la misma posición de "lista_binario" reemplazamos por '1'
        if numero >= lista[posicion]:
            lista_binario[posicion] = '1'
            numero -=  lista[posicion]
    #Transformamos la lista_binario en un string
    for i in lista_binario:
        numero_binario += i 
    return numero_binario


def binario_decimal(binario):
    """Recibe como parámetro un número binario de 10 o menos elementos, y devuelve su equivalente en decimal"""
    #Transformamos a string el parámetro en caso de ser ingresado como número
    binario = str(binario)
    ##Definimos la lista de valores equivalentes a las potencias con base 2 
    lista = [512,256,128,64,32,16,8,4,2,1]
    #En lista_decimal se van a almacenar los valores a ser sumados
    lista_decimal = []
    #Indice nos va a servir para referenciar la posición de la lista que vamos a agregar a lsita_decimal
    indice = 0
    #Recorremos binario en modo inverso
    for j in binario[::-1]:
        #En cada vuelta restamos 1 a indice para recorrer de modo inverso "lista"
        indice -=1
        if j == '1':
            #Si el valor es '1', agregamos a la lista_decimal el equivalente a la posición de "lista"
            lista_decimal.append(lista[indice])
    #Devuelve la suma de la lista generada
    return sum(lista_decimal)






