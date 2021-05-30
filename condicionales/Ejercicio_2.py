"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el 
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""
#from bullet import Password
import getpass
print("REACTIVACIÓN DE CONTRASEÑA")
password = getpass.getpass("Ingrese su nueva contraseña: ")
contra = getpass.getpass("Repita su contraseña: ")
if password == contra:
    print("Contraseña correcta")
else: 
    print("Contraseña incorrecta")



#cli = Password("Contraseña: ")
#p= cli.launch()

