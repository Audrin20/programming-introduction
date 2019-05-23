n = int(input('Digite um valor:'))
conth = 0
for i in range(1,n):
    h = 1 + 1/i
    conth = conth + h
    print(f'{h:.2f} ',end = '+ ')
print(f'= {conth:.2f}')