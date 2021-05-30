"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura 
la inversión."""

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = int(input("Ingrese el interés a ser generado por año (porcentaje): "))
anios = int(input("Ingrese la cantidad de años que desea invertir: "))

for anio in range(anios):
    cantidad = cantidad + (cantidad * interes / 100)
    print(f"Año {anio}: {cantidad}")