from random import randint
from time import sleep
computador=randint(0,10)
print("\033[33m-=-"*5,"JOGO DE ADIVINHAÇÃO","-=-"*5,"\033[0m")
print("\033[36mAcabei de pensar em um número entre 0 e 10.\n"
      "Será que você consegue adivinhar qual foi?")
sleep(1)
n=input("Qual o seu palpite?"+"\033[1;32m ")

while not n.isdigit():
      print("\033[31m"+"Entrada inválida, tente novamente!")
      n = input("\033[36m"+"Qual o seu palpite?"+"\033[1;32m ")
      

n = int(n)


count=1
while n != computador:
      if n > computador:
            print("\033[31m"+"Menos...\033[36m"+"Tente mais uma vez")
            n=int(input("\033[36m"+"Qual o seu palpite?"+"\033[1;32m "))
      
      elif n < computador:
            print("\033[31m"+"Mais... "+"\033[36m"+"Tente mais uma vez.") 
            n=int(input("\033[36m"+"Qual o seu palpite?"+"\033[1;32m "))
      count+=1
      
      

print("\033[32m"+"Você acertou com "+f"\033[1;97m {count} "+"\033[32m"+"tentativas. Parabéns!"+"\033[0m")
 

'''VERSÃO GUANABARA
from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('Analisando...'), sleep(3)
print('Você acertou com {} tentativas! Parabéns'.format(palpites))'''