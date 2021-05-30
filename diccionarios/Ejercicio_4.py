"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
diccionario = {1:"Enero", 
                2: "Febrero", 
                3:"Marzo", 
                4:"Abril", 
                5:"Mayo", 
                6:"Junio", 
                7:"Julio", 
                8:"Agosto",
                9:"Septiembre",
                10: "Octubre",
                11: "Noviembre",
                12: "Diciembre"}
#Transformo la fecha ingresada en una lista, eliminando el separador.
lista_fecha = fecha.split("/")
if len(lista_fecha) != 3:
    print("No es una fecha válida.")
else:
    print(f"{lista_fecha[0]} días del mes de {diccionario[int(lista_fecha[0])]} de {lista_fecha[2]}")

