numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite outro número: '))
if numero1 > numero2 and numero1 > numero3:
    print(f'O número {numero1} é o MAIOR entre os digitados')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O número {numero2} é o MAIOR entre os digitados')
else:
    print(f'O número {numero3} é o MAIOR entre os digitados')