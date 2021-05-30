"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y 
elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

materias = []
eliminar = []

while input("Desea agregar una materia? (s/n): ") == "s":
    materias.append(input("Ingrese el nombre de la materia: "))
else:
#Recorre la lista materias y pregunta la nota.
#Si es mayor o igual a 7 agrega a la lista eliminar.
    for materia in materias:
        if int(input(f"Qué nota obruvo en {materia}?: ")) >= 7:
            eliminar.append(materia)
#Recorre la lista eliminar, y remueve el elemento de la lista de materias.
    for materia in eliminar:
        materias.remove(materia)
print(f"Las materias desaprobadas son: {materias}")