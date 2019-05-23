V = []
contK = 0
K = int(input('Digite o valor da constante: '))
tam = int(input('Digite o tamanho do seu vetor: '))
for i in range(tam):
    num = int(input('Digite um número: '))
    V.append(num)
    if V[i] == K:
        contK+=1
print(f'Vetor: {V}')
print(f'Ocorrências de K em V: {contK}')