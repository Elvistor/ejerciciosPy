"""Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir."""

ingles_esp = {"house":"casa", "my":"mi", "green":"verde"}

while True:
    if input("Agregar? s/n: ") == "s":
        ing, esp = input("Ingrese una palabraen inglés y su traducción en español, separados por una coma: ").split(",")
        ingles_esp[ing] = esp
    else:
        frase = input("Ingrese una frase (ingrese 'salir' para terminar): ")
        if frase.lower() == "salir":
            break
        else:
            frase = frase.split(" ")
            for palabra in frase:
                try:
                    print(f"{ingles_esp[palabra]} ", end=True)
                except:
                    print(palabra, end=" ")
            break
print(" ")
