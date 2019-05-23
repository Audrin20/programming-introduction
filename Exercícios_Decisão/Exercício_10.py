print(24*'-')
print("BEM-VINDO AO DOM HENRIQUE'S HOTEL")
print('ESCOLHA SEU TIPO DE APARTAMENTO!')
print(24*'-')
print(' Tipo |  Valor Diária  |\n  A   |    R$150,00    |\n  B   |    R$100,00    |\n  C   |    R$75,00     |\n  D   |    R$50,00     |')
print(24*'-')
nome_hosp = input('Digite o nome do hóspede: ')
type_apto = input('Tipo de Apartamento escolhido:').upper()
num_diarias = int(input('Número de diárias: '))
consumo_inter = int(input('Consumo interno: R$'))
if (type_apto == 'A'):
    valor_apto = num_diarias * 150
if (type_apto == 'B'):
    valor_apto = num_diarias * 100
if (type_apto == 'C'):
    valor_apto = num_diarias * 75
if (type_apto == 'D'):
    valor_apto = num_diarias * 50
subtotal = (valor_apto + consumo_inter)
taxa_serv = (subtotal * 10)/100
total_geral = subtotal + taxa_serv
print(20*'-')
print('    NOTA FISCAL')
print(20*'-')
print(f'Nome do Hóspede: {nome_hosp}')
print(f'Tipo do Apartamento: {type_apto}')
print(f'Número de Diárias: {num_diarias}')
print(f'Valor total das diárias: R${valor_apto:.2f}')
print(f'Consumo Interno:R${consumo_inter:.2f}')
print(f'Subtotal: R${subtotal:.2f}')
print(f'Taxa de Serviço:R$ {taxa_serv:.2f}')
print(f'Total Geral: R${total_geral:.2f}')
print(20*'-')