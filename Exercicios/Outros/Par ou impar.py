from time import sleep
from termcolor import colored

n=int(input("Escolha um número ",))
sleep(1)
#n1=n/2
#if n1==int(n1)

if (n%2)==0:    # Todo numero divisel por 2 o modulo da 0 e é par, todo número impar vai dar 1
    print(colored("Seu número é par!",'green'))
else:
    print(colored("Seu número é impar!",'red'))
