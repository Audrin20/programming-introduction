while True:
    if temperatura > maior_temp:
        maior_temp = temperatura
    if temperatura < maior_temp:
        menor_temp = temperatura
print('mais quente:',maior_temp)
print('mais frio:',menor_temp)