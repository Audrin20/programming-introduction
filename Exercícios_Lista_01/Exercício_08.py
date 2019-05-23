print('MENU DE OPÇÕES:')
print('1)Cadastrar nome\n2)Pesquisar nome\n3)Listar todos os nomes\n0)Sair do Programa')
print(20*'-')
lista_nomes = []
op = int(input('Digite a opção:'))
while op != 0:
    if op == 1:
        nome = input('Digite o nome: ')
        lista_nomes.append(nome)
        op = int(input('Digite a opção:'))
    elif op == 2:
        nome = input('Digite o nome: ')
        if lista_nomes == []:
            print('Nenhum nome foi cadastrado')
        elif nome in lista_nomes:    
            print('O Nome está Cadastrado!!')
            print(f'- {nome}')
        else:
            print('Nome não cadastrado!!')
        op = int(input('Digite a opção:'))
    elif op == 3:
        print(f'Lista de nomes cadastrados: {lista_nomes}')
        op = int(input('Digite a opção:'))
    else:
        print('Opção Inválida, Tente outra vez')
        op = int(input('Digite a opção:'))
print('Programa Encerrado!')