"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con 
dominio ceu.es"""

mail = input("Ingrese su mail: ")
if "@" in mail:
    for letra in range(len(mail)):
        if mail[letra] == "@":
            nuevo_mail = mail[:letra] + "@ceu.es"
            print(nuevo_mail)
            break
else:
    print("No es un mail")
