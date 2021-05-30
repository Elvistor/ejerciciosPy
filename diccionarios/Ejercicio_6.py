"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una 
persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el 
contenido del diccionario."""


listado = {}

while True:
    if input("Desea agregar a una pesona? (s/n): ") == "s":
        persona = {}
        dni = int(input("Ingrese el D.N.I (sin puntos): "))
        persona["nombre"] = input("Ingrese el nombre: ")
        persona["apellido"] = input("Ingrese el apellido: ")
        persona["edad"] = int(input("Ingrese la edad: "))
        persona["sexo"] = input("Ingrese el sexo: ")
        persona["telefono"] = input("Ingrese el telefono: ")
        persona["mail"] = input("Ingrese el mail: ")
        listado[dni] = persona
        for identidad, datos in listado.items():
            print(f"""
            ----------------
            Nombre:   {datos["nombre"]}
            Apellido: {datos["apellido"]}
            Edad:     {datos["edad"]}
            Sexo:     {datos["sexo"]}
            Teléfono: {datos["telefono"]}
            E-mail:   {datos["mail"]}
            ----------------""")
    else:
        print("""Se ha finalizado la carga.""")
        break

