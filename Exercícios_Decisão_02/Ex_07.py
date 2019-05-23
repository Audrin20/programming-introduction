nota_prova1 = float(input('Digite a nota da 1ªprova:'))
nota_prova2 = float(input('Digite a nota da 2ªprova:'))
media_etapa1 = (nota_prova1 + nota_prova2)/2
if media_etapa1 >= 7:
   print('Apto para a 2ª etapa:')
   nota_prova1_etp2 = float(input('Digite a nota da 1ª prova da 2ª etapa:'))
   if nota_prova1_etp2 >= 8:
        print('Aprovado no Concurso')
   else:
        print('Reprovado')
else:
        print('Reprovado na 1ª etapa')