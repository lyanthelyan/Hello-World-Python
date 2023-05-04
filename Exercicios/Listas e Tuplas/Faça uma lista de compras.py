from time import sleep
import os

op=0
lista=[]
def menu():
    while True:
        print("Selecione uma opção")
        try:
            op=int(input(("[1] Inserir [2] Apagar [3] Listar [4] Sair: ")))
        except ValueError:
            print("\033[31mEntrada inválida. Tente novamente\033[0m")
            continue
        if op != 1 and op!= 2 and op!=3 and op != 4:
            print("\033[31mEntrada inválida. Tente novamente\033[0m")
#-------------------------------------------------------------------------    
        if op == 1:
            os.system('cls')
            inserir=input("O que você quer inserir? ")
            lista.append(inserir)
#------------------------------------------------------------------------
        try:
            if op == 2:
                os.system('cls')
                apagar=int(input("O que você quer apagar? "))
                del lista[apagar]
        except IndexError:
            print("Não foi possível apagar este índice.")
            continue
        except ValueError:
            print("Não foi possível apagar este índice.")
            continue
#-------------------------------------------------------------------------
        if op == 3:
            for indice, produtos in enumerate(lista):
                print(f'{indice}','-', f'{produtos}')
            if len(lista) == 0:
                print("Nada para listar")    
#-------------------------------------------------------------------------    
        if op == 4:
            print("Finalizando...")
            sleep(1)
            print("Obrigado volte sempre!")
            break

menu()