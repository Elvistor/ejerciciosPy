"""Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa 
no está en el diccionario."""

simbolo = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Qué moneda desea buscar?: ")
if moneda.capitalize() in simbolo.keys():
    print(f"El símbolo es {simbolo[moneda.capitalize()]}")
else:
    print("No se ha encontrado la moneda que busca.")
