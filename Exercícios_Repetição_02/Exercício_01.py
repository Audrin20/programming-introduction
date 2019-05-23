while True:
    print('----- Menu -----')
    print('1 - Saudação\n2 - Bronca\n3 - Felicitação\n0 - Fim')
    print('----------------')
    op_num = int(input('Digite uma opção: '))
    if op_num == 0:
        print('Fim de Serviço!!')
        break
    if op_num == 1:
        print('Olá. Como vai?')
    elif op_num == 2:
        print('Vamos estudar mais!!')
    elif op_num == 3:
        print('Meus Parabéns!')
    elif op_num > 3:
        print('Número INVÁLIDO')