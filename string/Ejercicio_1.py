"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

nombre = input("Ingrese el nombre que desee mostrar: ")
cantidad = int(input("Cuántas veces desea repetir?: "))

for repe in range(cantidad):
    print(nombre)
    
