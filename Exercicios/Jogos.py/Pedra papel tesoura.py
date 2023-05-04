from time import sleep
import random
print("Suas opções:")
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador=(int(input("Qual a sua jogada? ")))

jogadas=['Pedra', 'Papel', 'Tesoura']
computador=random.choice(jogadas)


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'*10)
print(f"Computador jogou {computador}!")
if jogador == 1:
    print(f"Jogador jogou Papel!")
elif jogador == 2:
    print(f"Jogador jogou Tesoura!")
elif jogador == 0:
    print(f"Jogador jogou Pedra! ")
print('-=-'*10)

if computador == jogadas[0] and jogador == 2:
    print('Computador Vence!')
elif computador == jogadas[1] and jogador ==0:
    print('Computador vence!')
elif computador == jogadas[2] and jogador == 1:
    print("Computador vence!")

elif jogador == 0 and computador == jogadas[2]:
    print('Jogador Vence!')
elif jogador == 1 and computador == jogadas[0]:
    print('Jogador vence!')
elif jogador == 2 and computador == jogadas[1]:
    print("Jogador vence!")

elif jogador == 0 and computador == jogadas[0]:
    print('Empate!')
elif jogador == 1 and computador == jogadas[1]:
    print('Empate!')
elif jogador == 2 and computador == jogadas[2]:
    print("Empate!")
    
elif jogador !=0 and jogador!=1 and jogador !=2:
    print('Jogador não escolheu uma opção coerente!')
    print('Computador Vence!')


    #print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
#a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
#b = random.randint(1,3)
#print (b)
#if a == b:
   ## print ("EMPATE")
#elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    #print ("VOCÊ PERDEU!")
#else:
    #print ("VOCÊ GANHOU")



