peso = float(input("Ingrese su peso expresado en kilogramos: "))
altura = float(input("Ingrese su altura expresado en metros: "))
imc = peso/pow(altura, 2)
print("""
Peso inferior al normal >>> Menos de 18.5
Peso normal             >>> 18.5 - 24.9
Peso superior al normal >>> 25.0 - 29.9
Sobrepeso               >>> Mas de 29.9""")
print(f"Su IMC es: {imc:.2f}")