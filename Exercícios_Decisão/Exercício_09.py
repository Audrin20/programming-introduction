indice_poluição = int(input('Digite o índice de poluição: '))
if indice_poluição >= 30 and indice_poluição < 40 :
    ind_pol = 'A L E R T A !\nIndústrias do grupo 1 devem suspender atividades!'
elif indice_poluição >= 40 and indice_poluição < 50:
    ind_pol = 'A L E R T A !\nIndústrias dos grupos 1 e 2 devem suspender as atividades!'
elif indice_poluição >= 50:
    ind_pol = 'A L E R T A !\nIndústrias dos grupos 1, 2 e 3 devem suspender as atividades!'
else: 
    ind_pol = 'Índice Aceitável!'
print(f'{ind_pol}')