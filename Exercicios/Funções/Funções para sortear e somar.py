import random
from time import sleep
def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = random.randint(0,10)
        lista.append(n)
        print(f'{n} ' , end='')
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = []
sorteio(numeros)
somapar(numeros)