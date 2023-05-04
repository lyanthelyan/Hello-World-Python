from time import sleep
n=0
continuar='s'
count=0
total=0
numeros=[]
while continuar == 's':   
    try:
        n=int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida tente novamente")
        continue
    continuar=input("Quer continuar? [S/N] ").lower().strip()[0]  #Considerar apenas a primeira letra
    numeros.append(n)   
    total+=n
    count+=1
    #media=total/count
    while continuar != 's' and continuar != 'n':
        print("Entrada inválida tente novamente")
        continuar=input("Quer continuar? [S/N] ").lower().strip()[0]            
    if continuar == 'n':
        print("Finalizando...")
        sleep(1.2)
media=total/count        
print(f'A média é igual à {media}')
print(f"O maior número é {max(numeros)} e o menor número é {min(numeros)}")
    

