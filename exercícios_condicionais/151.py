peso = int(input("insira o peso"))
altura = float(input("insira a altura"))

imc = peso/altura**2

if imc<20:
    print("abaixo do peso")
elif imc <=25:
    print("normal")
elif imc <= 30:
    print("excesso de peso")
elif imc <= 35:
    print("obesidade")
else:
    print("obesidade mórbida")
