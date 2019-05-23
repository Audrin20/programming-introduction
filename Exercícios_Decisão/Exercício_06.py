hora_inicio = int(input('Digite a hora inicial do jogo: '))
hora_final = int(input('Digite a hora final do jogo: '))
if hora_inicio >= hora_final:
    duracao = (24 - hora_inicio) + hora_final
else:
    duracao = hora_final - hora_inicio
print(f'Tempo de duração da partida {duracao}h')