import random

print("=-"*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
count=0

while True:
    try:
        valor=int(input("Diga um valor: "))
    except ValueError:
        print('=-'*13)
        print("Entrada Inválida. Tente novamente")
        print('=-'*13)
        continue
    
    par_impar=input("Par ou Ímpar? [P/I] ").lower()
    random_numeros=random.randint(1,10)
    
    if par_impar != 'p' and par_impar != 'i':
        print('=-'*13)
        print("Entrada Inválida. Tente novamente")
        print('=-'*13)
        continue
    
    if par_impar =='p':
        resultado=random_numeros + valor      
        if resultado % 2 == 0:
            print(f"Você jogou {valor} e o computador {random_numeros}. Total de {resultado}")
            print('=-'*13)
            print(f"Você Venceu!")
            print("Vamos jogar novamente...")
            print('=-'*13)
            count+=1
        
        if resultado % 2 != 0:
            print(f"Você jogou {valor} e o computador {random_numeros}. Total de {resultado}")
            print("Você Perdeu")
            print(f"Você venceu {count} vezes")
            print('=-'*13)
            break           
    
    if par_impar =='i':
        resultado=random_numeros + valor
        if resultado % 2 == 1:
            print(f"Você jogou {valor} e o computador {random_numeros}. Total de {resultado}")
            print('=-'*13)
            print(f"Você Venceu!")
            print("Vamos jogar novamente...")
            print('=-'*13)
            count+=1
    
        if resultado % 2 !=1:
            print(f"Você jogou {valor} e o computador {random_numeros}. Total de {resultado}")
            print("Você Perdeu!")
            print(f"Você venceu {count} vezes")
            print('=-'*13)
            break
            



