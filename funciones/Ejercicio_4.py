"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

#Si no recibe iva como parámetro, se encuentra predeterminado el 21%
def calcularIVA(monto, iva=21):
    """Recibe un monto y el iva representado en porcentaje, y los multiplica"""
    total = monto + (monto * (iva/100))
    return total


