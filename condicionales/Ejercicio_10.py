"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un 
ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe 
mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

respuesta = input("Desea una pizza Vegetariana? s/n: ")
if respuesta == "s":
    pizza = "Vegetariana"
    tipo = ["Pimiento", "Tofu"]
    ingrediente = int(input("""Seleccione un ingrediente:
    0. Pimiento
    1. Tofu
    """))
else:
    pizza = "No Vegetariana"
    tipo = ["Peperoni", "Jamón", "salmón"]
    ingrediente = int(input("""Seleccione un ingrediente:
    0. Peperoni
    1. Jamón
    2. Salmón
    """))

print(f"Su pedido es una pizza {pizza}, y los ingredientes son: Mozzarella, tomate y {tipo[ingrediente]}")