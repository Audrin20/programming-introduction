vetor1 = []
vetor2 = []
lista = []
for i in range(10):
    num = int(input('Digite um número: '))
    vetor1.append(num)
for i in range(len(vetor1)):
    if i % 2 == 0:
        vetor2.append(vetor1[i] * 2)
    else:
        vetor2.append(vetor1[i] * 3)
print(f'V E T O R   O R I G I N A L = {vetor1}')
print(f'VETOR PARES 2x | ÍMPARES 3x = {vetor2}')