quant = input('\nDigite a quantidade de fitas: ')
valAluguel = float(input('\nDigite o valor do aluguel: '))

fatAnual = quant/3 * valAluguel * 12

print(f'Faturamento anual: {fatAnual}')

multas = valAluguel * 0.1 * (quant/3) / 10

print(f'Multas mensais: {multas}')

quantFinal = (quant - quant * 0.02 + quant/10)

print(f'Quantidade de fitas no final do ano: {quantFinal}')
