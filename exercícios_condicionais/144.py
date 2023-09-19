saldomedio = int(input("digite o saldo médio \n"))

if saldomedio < 501:
    credito = 0
elif saldomedio < 1001:
    credito = saldomedio * 0.3
elif saldomedio < 3001:
    credito = saldomedio * 0.4
else:
    credito = saldomedio * 0.5

if credito != 0:
    print(f"Como seu saldo era de {saldomedio} seu credito será {credito}")
else:
    print(f"Como seu saldo era de {saldomedio} você não terá nenhum crédito")