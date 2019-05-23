nome = str(input('Digite o seu nome: '))
saldo_medio_client = float(input('Digite o seu saldo médio: R$'))
calc_val_credito = 0
if saldo_medio_client >= 0 and saldo_medio_client <= 200:
    print('Nenhum Crédito')
elif saldo_medio_client >= 201 and saldo_medio_client <= 400:
    calc_val_credito = (saldo_medio_client * 20) / 100
    print('Crédito: 20% do valor do seu saldo médio.')
elif saldo_medio_client >= 401 and saldo_medio_client <= 600:
    calc_val_credito = (saldo_medio_client * 30) / 100
    print('Crédito: 30% do valor do seu saldo médio.')
else:
    calc_val_credito = (saldo_medio_client * 40) / 100
    print('40% do valor do seu saldo médio.')
print(40*'-')
print('E X T R A T O')
print(40*'-')
print(f'Nome: {nome}')
print(f'Saldo Médio: R${saldo_medio_client:.2f}')
print(f'Valor disponível para crédito: R${calc_val_credito:.2f}')
print(40*'-')