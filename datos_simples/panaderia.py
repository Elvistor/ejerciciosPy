print("------------------")
print("%PANADERÍA EL PAN%")
print("------------------")
cantidad = int(input("Cantidad de panes no frescos?: "))
valor_actual = float(3.49 * 0.4) 
cant_total = cantidad * valor_actual
print (f"""Si se venden {cantidad} panes con un descuento de {3.4 - valor_actual : .2f}€
se recaudan un total de {cant_total}€""") 