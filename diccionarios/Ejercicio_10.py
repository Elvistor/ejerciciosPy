"""Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.

Genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. """

#Clientes va a tener como key a los NIF, y cada NIF va a contener datos

cliente = {}
#En opción se almacena la opción ingresada, para posteriores comparaciones
opcion = ''
while opcion != '6':
    print('Ingrese una opción: ')
    print("""
    -------------------------------
    1) Añadir cliente
    2) Eliminar cliente
    3) Mostrar cliente
    4) Listar todos los cliente
    5) Mostrar clientes preferentes
    6) Terminar
    -------------------------------
    """)
    
    opcion = input('')
    #Añadir cliente
    if opcion == '1':
        #Datos va a contener nombre, direccion, telefono, correo y preferente
        datos = {}
        nif = input('ingrese el NIF del cliente: ')
        if nif not in cliente:
            print('Ingrese los datos del cliente:')
            datos['nombre'] = input('Nombre: ')
            datos['direccion'] = input('Dirección: ')
            datos['telefono'] = input('Teléfono: ')
            datos['correo'] = input('E-mail: ')
            preferente = input('Es un cliente preferente? (s/n): ')
            #Guardamos True o False dependendiendo de la respuesta del usuario
            if preferente == 's':
                datos['preferente'] = True
            else:
                datos['preferente'] = False
            cliente[nif] = datos
            print('Cliente agregado de forma exitosa!!!!')
            print('')
        else:
            print('Ya se encuentra registrado esa clave')

    #Eliminar cliente    
    elif opcion == '2':
        eliminar = input('Ingrese el NIF del cliente a eliminar: ')
        if eliminar in cliente:
            for dato, info in cliente[eliminar].items():
                #mostramos cada elemento del diccionario
                print(f"""
                {dato}: {info}
                """) 
            del cliente[eliminar]
            print('Se eliminó de forma correcta')
            print('')
        else:
            print('La clave no se encuentra registrada')

    #Mostrar cliente
    elif opcion == '3':
        print('Qué cliente desea buscar?: ')
        nif = input('')
        if nif in cliente:
            for clave, valor in cliente[nif].items():
                print(f"""
                {clave}: {valor}""")
        else:
            print('La clave no se encuentra registrada')
            print('')
    #Listar clientes
    elif opcion == '4':
        #Clave va a almacenar cada nif, y valor va a almacenar el diccionario de datos
        #Recorremos cada elemento del diccionario de clientes
        for clave,valor in cliente.items():
            #Mostramos cada nif
            print(f"""
            NIF: {clave}""")
            print('Nombre: ', valor['nombre'])
            print('--------------')
    #Cliente VIP        
    elif opcion == '5':
        print('Clientes VIP')
        for clave,valor in cliente.items():
            if valor['preferente'] == True:
                print(f"""
                NIF: {clave}
                Nombre: {valor['nombre']}""")
    #Terminar
    else:
        print('Gracias')
        break
