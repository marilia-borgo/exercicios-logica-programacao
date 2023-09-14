valor = input("digite o valor da prestação")
taxa = input("digite a taxa")
tempo = input("digite o numero de meses")

prest = valor+(valor*(taxa/100)*tempo)
print("o valor da prestação em atraso é =", prest)