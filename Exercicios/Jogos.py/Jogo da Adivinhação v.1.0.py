import random
import time
computador = (0,1,2,3,4,5)
ale=random.choice(computador)

numero=int(input("Vou pensar em um número de 0 a 5! Tente adivinhar..."))
print("Processando...")
time.sleep(2)

if ale == numero:
    print("Eu perdi, eu pensei exatamente nesse número")
else:
    print(f"Eu ganhei!, eu pensei no número {ale} e não no {numero}!")

#print(f"Pensei no número {ale}")



from random import randint
from time import sleep

computador = randint(0,5)
print('-=-'*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
sleep(3)
if jogador==computador:
    print('Parabéns! você conseguiu me vencer!')
else:
    print(f"Ganhei! Eu pensei no número {computador} e não no {jogador}!")