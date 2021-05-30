"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

import getpass
print("REACTIVACIÓN DE CONTRASEÑA")
password = getpass.getpass("Ingrese su nueva contraseña: ")
while password != getpass.getpass("Ingrese nuevamente: "):
    print("No coinciden, intentar nuevamente")
else:
    print("Correcto!")