senha_K = '88888888'
cont_senha = 0
while True:
    senha = input('Digite a senha (8 char):')
    if senha == senha_K:
            print('Senha correta!')
            break
    cont_senha += 1
    if cont_senha != 3:
        if senha == senha_K:
            print('Senha correta!')
            break
        else:
            print('Senha incorreta!')
    else:
        print('Senha incorreta!')
        print('Acesso Negado')
        break
print('Fim')