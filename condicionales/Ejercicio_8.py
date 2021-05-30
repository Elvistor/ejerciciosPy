"""Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario."""

puntuacion = float(input("Ingrese puntuación: "))
if puntuacion == 0.0:
    print(f"Nivel: Inaceptable, Monto a recibir $0")
elif puntuacion == 0.4:
    print(f"Nivel: Aceptable, Monto a recibir ${puntuacion * 2400}")
elif puntuacion >= 0.6:
    print(f"Nivel: Meritorio, Monto a recibir ${puntuacion * 2400}")
else:
    print("No es un valor válido")