num = int(input('Digite número:'))
cont_maior = num
cont_menor = num
for i in range(1,5):
    if num == 0:
        break
    else:
        num = int(input('Digite número:'))
        if num > cont_maior:
            cont_maior = num
        if num < cont_menor:
            cont_menor = num
print(f'Maior:{cont_maior}')
print(f'Menor:{cont_menor}')
    

