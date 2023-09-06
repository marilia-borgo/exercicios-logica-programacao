sm = input("entre com o salário mínimo")

qtdade = input("etr com a quantidade em quilowatt")

preco = int(sm)/700
vp = preco/int(qtdade)
vd = vp * 0.9

print(f"preço do quilowtt {preco}, valor a ser pago {vp}, valor com desconto {vd}")