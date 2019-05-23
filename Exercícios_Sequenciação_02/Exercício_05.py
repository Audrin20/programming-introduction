Valor = 11257

nota100 = Valor // 100
resto = Valor % 100

nota50 = resto // 50
resto = Valor % 50

nota20 = resto // 20
resto = Valor % 20

nota10 = resto // 10
resto = Valor % 10

nota5 = resto // 5
resto = Valor % 5

nota2 = resto // 2
resto = Valor % 2

nota1 = resto // 1
resto = Valor % 1

print(f'{nota100} Notas de R$100,00' )
print(f'{nota50} Notas de R$50,00')
print(f'{nota20} Notas de R$20,00')
print(f'{nota10} Notas de R$10,00')
print(f'{nota5} Notas de R$5,00')
print(f'{nota2} Notas de R$2,00')
print(f'{nota1} Notas de R$1,00')