num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
for i in range(num2,num3):
    if num3 % num1 == 0:
        multiplo = num1 / i+1
        print(multiplo)
