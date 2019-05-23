cont_mulher = 0
cont_homem = 0
cont_solteiros = 0
cont_casados = 0
salario_medio_m = 0
mulher_solteira_2000 = 0
media_idade_h = 0
idade_homens = 0
salario_medio_mulh = 0
homem_35_2000 = 0
while True:
    nome = input('Digite o seu nome:')
    if nome == '0':
        break
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo[M/F]: ')
    estado_civil = input('Digite o seu estado civil solteiro(a) ou casado(a): ').upper()
    salario = float(input('Digite o seu salário: R$'))
    if sexo == 'F':
        cont_mulher+=1
        salario_medio_m += salario
        salario_medio_mulh = salario_medio_m/cont_mulher
    else:
        cont_homem+=1
    if estado_civil == 'SOLTEIRO':
        cont_solteiros += 1
    else:
        cont_casados += 1
    if sexo == 'M':
        idade_homens += idade
        media_idade_h = idade_homens/cont_homem
    if  estado_civil == 'SOLTEIRA' and salario > 2000:
        mulher_solteira_2000 += 1
    if sexo == 'M' and idade > 35:
        homem_35_2000 += 1
    print('!!! -- NOVO REGISTRO -- !!!')
print(40*'-')
print('R E S U L T A D O  P E S Q U I S A')
print(40*'-')
print(f'Mulheres entrevistadas: {cont_mulher}')
print(f'Homens entrevistados: {cont_homem}')
print(f'Pessoas Solteiras:{cont_solteiros}')
print(f'Pessoas casadas: {cont_casados}')
print(f'Salário medio mulheres: {salario_medio_mulh}')
print(f'Média da idade dos Homens: {media_idade_h}')
print(f'Solterias ganham > R$2000.00: {mulher_solteira_2000}')
print(f'Homens + 35 anos que ganham > R$2000.00: {homem_35_2000}:')