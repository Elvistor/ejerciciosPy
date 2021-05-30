"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""

altura = int(input("Ingrese la altura del triángulo: "))
count = []
for i in range(altura):
    count.append(2*i+1)
    for j in range(i+1):
        count_reves = count[::-1]
        print(count_reves[j], end="")
    print()