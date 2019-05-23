salario = float(input('Digite o seu salário: R$'))
salario_minimo = 980
numero_vendas = float(input('Digite o número de vendas: R$'))
comissao = numero_vendas * 0.05
if comissao > salario_minimo:
    print(f'Sua comissão este mês foi de R${comissao:.2f}')
    print(f'Total ganhos mensal: R${salario + comissao:.2f}')
else:
    print(f'Total de ganhos mensal:R${salario:.2f}')
    print(f'Não teve comissao')