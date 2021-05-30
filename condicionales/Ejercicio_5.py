"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales 
o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""
try:
    edad = int(input("Ingrese su edad: "))
    ingreso = float(input("Ingrese el monto mensual: €"))

    if edad > 16 and ingreso > 1000:
        print("Se encuentra habilitado")
    else:
        print("No se encuentra habilitado")

except ValueError:
    print("El valor ingresado no es un número")
except NameError:
    print("Ingrese los valores de forma correcta")