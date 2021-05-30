"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura,
 y después las muestre por pantalla con el mensaje 
 En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas 
 de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

materias = []

while input("Desea agregar una materia? (s/n): ") == "s":
    materias_notas = []
    materias_notas.append(input("Ingrese el nombre de la materia: "))
    materias_notas.append(int(input("Ingrese la nota: ")))
    materias.append(materias_notas)
else:
    for materia,nota in materias:
        print(f"En {materia} has sacado {nota} ")
