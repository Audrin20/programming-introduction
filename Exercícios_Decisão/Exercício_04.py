idade_nadador = int(input('Digite a idade: '))
if idade_nadador >= 5 and idade_nadador <= 7:
    print('infantil A')
elif idade_nadador >= 8 and idade_nadador <= 10:
    print('Infantil B')
elif idade_nadador >= 11 and idade_nadador <= 13:
    print('Juvenil A')
elif idade_nadador > 14 and idade_nadador <= 17:
    print('Juvenil B')
elif idade_nadador > 18:
    print('Adulto')
else:
    print('IDADE INVÁLIDA')