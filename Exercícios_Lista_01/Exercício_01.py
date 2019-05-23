A = []
B = []
vetor = int(input('Digte o tamanho do vetor a ser formado: '))
K = int(input('Digite o valor da sua constante: '))
for  i in range(vetor):
    num = int(input('Digite os números do vetor: '))
    A.append(num)
    B.append(num*K)
print(f'A = {A}')
print(f'B = {B}')