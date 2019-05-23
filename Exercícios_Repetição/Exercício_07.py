fat = int(input('Digite o valor fatorial: '))
cont = fat
for i in range(1,fat):    
    fat*=i
print(f'{cont}! = {fat}')