val_segun = int(input('Digite os segundos:'))

horas = val_segun // 3600
resto = val_segun % 3600

minu = resto // 60
resto = val_segun % 60

segun = resto // 1
print(f'{horas:02d}:{minu:02d}:{segun:02d}')