nota_1 = float(input('Digite 1ª nota: '))
nota_2 = float(input('Digite 2ª nota: '))
nota_3 = float(input('Digite 3ª Nota: '))
nota_4 = float(input('Digite 4ª Nota: '))
if (nota_1 < nota_2) and (nota_1 < nota_3) and (nota_1 < nota_4):
    media = (nota_2 + nota_3 + nota_4)/3
elif (nota_2 < nota_1) and (nota_2 < nota_3) and (nota_2 < nota_4):
    media = (nota_1 + nota_3 + nota_4)/3
elif (nota_3 < nota_1) and (nota_3 < nota_2) and (nota_3 < nota_4):
    media = (nota_1 + nota_2 + nota_4)/3
else:
    media = (nota_1 + nota_2 + nota_3)/3
print(f'Media do Aluno:{media:.1f}')