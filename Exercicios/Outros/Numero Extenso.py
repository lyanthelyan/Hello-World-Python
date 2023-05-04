numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove','dez',
          'onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
#-------------------------------------------------------------------------------------------------------
'''resposta = -1
while resposta not in range(0,21):
    resposta=int(input("Digite um número entre 0 e 20: "))
    while resposta not in range(0,21):
        resposta = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    if resposta in range(0,21):
        break       
print(f"Você digitou o número {numeros[resposta]}")'''
#---------------------------------------------------------------------------------
'''while True:
    num=int(input("Digite um número entre 0 e 20: "))
    if 0<=num<=20:
        break
    print("Tente novamente. ",end='')
print(f"Você digitou o número {numeros[num]}")'''
#-----------------------------------------------------------
num=int(input("Digite um número entre 0 e 20: "))
while num not in range(0,20):
    num=int(input("Tente novamente. Digite um número entre 0 e 20"))
print(f"Você digitou o número {numeros[num]}")

    
    

