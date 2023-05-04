from random import randint
from time import sleep
from operator import itemgetter

# for i in range(4):
#     dado = randint(1, 6)
#     print(dado)

jogadores = {}

jogadores['jogador1'] = randint(0,6)
jogadores['jogador2'] = randint(0,6)
jogadores['jogador3'] = randint(0,6)
jogadores['jogador4'] = randint(0,6)
ranking = {}
for j, n in jogadores.items():
    print(f'{j} tirou {n} no dado.')
    #sleep(0.7)
print('-='*20)
print('==  RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'{k+1} lugar: {v[0]} com {v[1]}')
