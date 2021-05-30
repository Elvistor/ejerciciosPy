"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar."""

x = (1,2,3)
y = (-1,0,2)
prod_escalar = 0
for a in range(len(x)):
    prod_escalar += x[a] * y[a]
print(f"El producto escalar de x e y es: {prod_escalar}")