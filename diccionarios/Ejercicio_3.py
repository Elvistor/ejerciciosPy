"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese 
número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""

diccionario = {"platano":1.85, "manzana":0.80, "pera":0.85,"naranja":0.70}
fruta = input("Qué fruta desea agregar?: ")
cantidad = int(input("Cantidad? (kilogramos): "))
if fruta.lower() in diccionario.keys():
    total = diccionario[fruta.lower()] * cantidad
    print(f"Total: ${total: .2f}")
else:
    print("No se encuentra registrado esa fruta.")