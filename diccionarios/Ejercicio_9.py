"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""


facturas_pendientes = {}
total = 0


def seleccione_opcion():
    print("----------")
    print("Seleccione una opción:")
    opcion = input("""
    1. Añadir una factura
    2. Pagar una factura
    3. Terminar
    """)
    return opcion

eleccion = seleccione_opcion()
while eleccion != "3":#Mientras sea diferente de 3

    #Agregar factura y mostrar el total a pagar
    if eleccion == "1":
        nro_factura = input("Ingrese el número de factura: ")
        #Se agrega la factura
        facturas_pendientes[nro_factura] = float(input("Ingrese el monto: "))
        print(f"Actualmente debe pagar un total de: {sum(facturas_pendientes.values()): .2f}")
        eleccion

    #Pagar y eliminar factura, además, mostrar el total pagado y el restante
    elif eleccion == "2":
        
        try:#Capturar error de clave

            factura = input("Ingrese el número de factura: ")
            print(f"El monto a abonar es ${facturas_pendientes[factura]}, desea continuar?: ")
            continuar = input("(s/n): ")

        except KeyError:
            print("Factura no encontrada")
            continuar = ""
            eleccion
        #Si acepta continuar
        if continuar == "s":
            #Sumar el total abonado, mostrar y lo restante
            total += float(facturas_pendientes[factura])
            print(f"El total abonado hasta el momento es: ${total: .2f}")
            del facturas_pendientes[factura]
            print(f"Actualmente debe pagar un total de: {sum(facturas_pendientes.values()): .2f}")
            eleccion
        else:
            eleccion  

    elif eleccion == "4":
        print("Opción incorrecta, intente nuevamente.")
        eleccion


print("Gracias!!")


