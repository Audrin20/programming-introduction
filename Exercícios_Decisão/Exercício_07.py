peso = float(input('Digite Peso: '))
altura = float(input('Digite Altura: '))
imc = peso/altura**2
print('Grau de Obesidade:')
if imc < 26:
    print('Normal')
elif imc >= 26 and imc < 30:
    print('Obeso')
else:
    print('Obeso Mórbido')