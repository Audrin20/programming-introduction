matricula = int(input('Digite sua Matricula: '))
nota1 = float(input('Digite a 1ª Nota: '))
nota2 = float(input('Digite a 2ª Nota: '))
nota3 = float(input('Digite a 3ª Nota: '))
media_exerc = float(input('Digite a média dos exercícios: '))
media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exerc)/7
if media_aproveitamento >= 9:
    conceito = 'Conceito A\nAprovado'
elif media_aproveitamento >= 7.5 and media_aproveitamento < 9:
    conceito = 'Conceito B\nAprovado'
elif media_aproveitamento >= 6 and media_aproveitamento < 7.5:
    conceito = 'Conceito C\nAprovado'
elif media_aproveitamento >= 4 and media_aproveitamento < 6:
    conceito = 'Conceito D\nReprovado'
else:
    conceito = 'Conceito E\nReprovado'
print(20*'-')
print('BOLETIM')
print(20*'-')
print(f'Aluno - Nº matrícula: {matricula}')
print(f'Média de aproveitamento: {media_aproveitamento:.2f}')
print(conceito)