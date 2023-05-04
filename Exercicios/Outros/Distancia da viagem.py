from time import sleep
from termcolor import colored

d=float(input("Qual a distância da sua viagem?: "))

if d<= 200:
    p=d*0.50
else:
    p=d*0.45

print(colored(f"Você irá fazer uma viagem de {d}Km e irá custar...","blue"))
sleep(1)
print(colored("Processando...",'red'))
sleep(1)
print(colored("Processando...",'red'))
sleep(1)
print(colored("Processando...",'red'))
sleep(1)
print(colored(f"R${p:.2f}",'green'))

