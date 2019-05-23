while True:
    matricula = int(input('Digite sua matrícula: '))
    if matricula == 0:
        break
    nome = input('Digite o seu nome: ')
    nota1 = float(input('Digite nota 1:'))
    nota2 = float(input('Digite nota 2:'))
    media = (nota1 + nota2)/2
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    print(6*'-','BOLETIM',6*'-')
    print(f'Matrícula: {matricula}')
    print(f'Nome: {nome}')
    print(f'Média: {media:.1f}')
    print(f'Situação: {situacao}')
print('Fim do Programa')