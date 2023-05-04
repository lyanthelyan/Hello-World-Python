from time import sleep
import termcolor

speed=int(input("Qual a sua velocidade atual? "))

print(termcolor.colored('Processando...','green'))
sleep (2.5)
if speed >= (80):
    print(termcolor.colored(f"Multado!, você ultrapassou o limite de 80km/h",'red'))
    sleep(1)
    multa=(speed-80)*7
    print(termcolor.colored(f"Você deve pagar R${multa:.2f}!",'red'))
    sleep(0.5)
    print(termcolor.colored("Por favor dirija com segurança!",'green'))

else:
    print(termcolor.colored(f"Parabéns você está no limite de velocidade!",'green'))


