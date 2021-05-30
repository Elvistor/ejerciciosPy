"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	        5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	        45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""

monto = float(input("Ingrese el monto: "))
if monto < 10000:
    print(f"El impuesto es: {monto * 0.05: .2f}")
elif 10000 <= monto < 20000:
    print(f"El impuesto es: {monto * 0.15: .2f}")
elif 20000 <= monto < 35000:
    print(f"El impuesto es: {monto * 0.20: .2f}")
elif 35000 <= monto < 60000:
    print(f"El impuesto es: {monto * 0.30: .2f}")
else:
    print(f"El impuesto es: {monto * 0.45: .2f}")
