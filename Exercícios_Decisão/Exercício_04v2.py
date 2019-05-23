idade_nadador = int(input('Digite a idade: '))
categoria = 'SEM CATEGORIA'
if idade_nadador >= 5 and idade_nadador <= 7:
    categoria = 'infantil A'
elif idade_nadador >= 8 and idade_nadador <= 10:
    categoria = 'infantil B'
elif idade_nadador >= 11 and idade_nadador <= 13:
    categoria = 'Juvenil A'
elif idade_nadador > 14 and idade_nadador <= 17:
    categoria = 'Juvenil B'
elif idade_nadador > 18:
    categoria = 'Adulto'
else:
    print('IDADE INVÁLIDA')
print(f'categoria do atleta --> {categoria}')