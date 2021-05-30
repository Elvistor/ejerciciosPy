ahorro = float(input("Ingrese el monto a depositar en la caja de ahorro: "))
anio_1 = ahorro + (ahorro * (4/100))
anio_2 = anio_1 + (anio_1 * (4/100))
anio_3 = anio_2 + (anio_2 * (4/100))

print(f"""
Con una inversión de ${ahorro} pesos ud obtiene un retorne de:
Primer año: ${anio_1 : ,.2f}
Segundo año: ${anio_2 : ,.2f}
Tercer año: ${anio_3 : ,.2f}""")
