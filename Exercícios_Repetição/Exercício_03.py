num = int(input('Digite um número:'))
res = 0
for i in range(1,num+1,1):
    res = res + i
print(f'A soma da sequência de 1 à {num} = {res}')
