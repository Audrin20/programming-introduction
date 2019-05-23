numero_1 = int(input('Digite um número:'))
numero_2 = int(input('Digite outro número:'))
opera = input('Digite o sinal da operação:')
if opera == '+':
    resultado = numero_1 + numero_2
elif opera == '-':
    resultado = numero_1 - numero_2
elif opera == '/':
    resultado = numero_1 / numero_2
elif opera == '*':
    resultado = numero_1 * numero_2
elif opera == '%':
    resultado = numero_1 % numero_2
else:
    resultado = 'Operador Desconhecido'
print(f'O Resultado = {resultado}')
