altura = float(input('Digite a sua altura:'))
sexo = input('Digite o seu sexo: ')
peso_ideal = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7
if sexo == 'M':
    print(f'Peso ideal para homens = {peso_ideal:.1f}')
else:
    print(f'Peso ideal para mulheres = {peso_ideal_m:.1f}')
