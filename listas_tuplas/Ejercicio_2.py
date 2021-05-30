"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por 
pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas 
de la lista."""

materias = []
while input("Desea agregar una materia?: ") == "s":
    materias.append(input("Ingrese el nombre de la materia: "))
else:
    for materia in materias:
        print("Yo estudio: ",materia)