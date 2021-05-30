try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    cociente = num1 // num2
    resto = num2 % num2
    print(f"{num1} entre {num2} da un cociente {cociente} y un resto {resto}")
except ZeroDivisionError as divcero:
    print ("No se puede dividir por cero")
except SyntaxError as errorSyntaxys:
    print("Error de Sintaxis")