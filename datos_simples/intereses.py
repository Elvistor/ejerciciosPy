monto = float(input("Ingrese el monto a invertir en pesos: "))
intereses = float(input("Ingrese el interés generado (expresado en %): "))
años = int(input("Cuántos años desea ingresar?: "))
total = monto*intereses*años
print(f"Dentro de {años} años, con una inversión de {monto} tendrá un total de {total} pesos")