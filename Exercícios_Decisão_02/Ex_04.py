dia = int(input('Digite um número (1 a 7):'))
if dia == 1:
    semana = 'Domingo'
elif dia == 2:
    semana = 'Segunda'
elif dia == 2:
    semana = 'Terça'
elif dia == 2:
    semana = 'Quarta'
elif dia == 2:
    semana = 'Quinta'
elif dia == 2:
    semana = 'Sexta'
else:
    semana = 'Sábado'
print(semana)
if dia > 1 and dia < 7:
    print('Dia útil')
else:
    print('Final de Semana')
