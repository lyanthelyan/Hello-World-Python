num=int(input("Digite um número: "))

count=0  
for c in range(1, num+1):
    if (num % c ==0):
        print('\033[32m', end='')
        count=count+1                              
    else:
        print('\033[31m', end='')
    
    print(f'{c}', end=' ')
print(f'\n\033[34mO número {num} foi divisível {count} vezes')
if count == 2:
    print("\033[33mE por isso ele é primo")
else:
    print("\033[33mE por isso ele não é primo")
