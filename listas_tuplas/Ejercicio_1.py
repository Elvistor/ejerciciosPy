"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla"""

materias = []
while input("Desea agregar una materia?: ") == "s":
    materias.append(input("Ingrese el nombre de la materia: "))
else:
    print(materias)