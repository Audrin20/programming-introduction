gab = [5, 1, 2, 3, 5, 4, 5, 2, 1, 3]
prova = []
cont_correta = cont_errada = 0
print('Prova do Tio Audrin')
for i in range(10):
    resp = int(input(f'Alternativa {i+1}:'))
    prova.append(resp)
    if gab[i] == prova[i]:
        cont_correta += 1
    else:
        cont_errada += 1       
print(f'G A B A R I T O: {gab}')
print(f'P R O V A: {prova}')
print(f'Correta(s): {cont_correta}')
print(f'Errada(s): {cont_errada}')