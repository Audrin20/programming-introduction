num = int(input('Digite qualquer valor:'))
conta_maior = num
conta_menor = num
while num != 0:
    if num > conta_maior:
        conta_maior = num
    if num < conta_menor:
        conta_menor = num
    num = int(input('Digite outro valor:'))
print(f'Maior Valor: {conta_maior}')
print(f'Menor Valor: {conta_menor}')