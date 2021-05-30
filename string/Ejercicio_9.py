"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter."""

from datetime import datetime
fecha = input("Ingrese su fecha de nacimiento, con formato dd/mm/aaaa: ")
fecha = datetime.strptime(fecha, '%d/%m/%Y')
print(f"""Día: {fecha.day}
Mes: {fecha.month}
Año: {fecha.year}""")