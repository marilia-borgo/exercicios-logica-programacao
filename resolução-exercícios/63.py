na = input("horas trabalhadas:")
vha = input("valor da hora-aula")
pd = input("porcntual de desconto")

sb = na*vha
td = (pd /100) * sb
sl = sb - td

print("salario liquido", sl)