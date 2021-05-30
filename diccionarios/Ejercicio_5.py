"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> 
es cada una de las asignaturas del curso, y <créditos> son sus créditos.
 Al final debe mostrar también el número total de créditos del curso."""

materias_creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
#Con item() itero el diccionario por elementos.
for materia,credito in materias_creditos.items():
    print(f"{materia} tiene {credito} créditos.")
    total += credito
print(f"Tiene un total de {total} créditos en curso.")
