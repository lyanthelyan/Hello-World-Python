from time import sleep
def maior(* num): # Os asteristicos indica que irá ter mais de um valor
    if len(num) == 0:
        print('-='*30)
        print("Nenhum valor foi informado.")
        return
       
    cont = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end ='')
        sleep(0.3)
        cont+=1
    print(f' Foram informados {cont} valores ao todo.')

    print(f"O maior valor informado foi o {max(num)}.")
    
        

# Programa Principal
maior(6)

maior(0)

maior()