"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario 
con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total 
con 8 dígitos enteros y 2 decimales."""
producto = input("Ingrese el producto: ")
precio = float((input("Ingrese el precio: ")))
cantidad = int((input("Ingrese la cantidad: ")))
total = precio * cantidad
print(f"""El producto {producto} cuesta $ {precio: 6.2f}, se vendieron un total de {cantidad: ,}
lo que da un total de $ {total: 8.2f}""")