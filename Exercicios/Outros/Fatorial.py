from math import factorial
n=int(input("Digite um número para calcular seu Fatorial: "))
count=n
print(f"{n}! = ", end='')
while count> 0:
    
    print(f"{count}",end='')
    print(" x " if count > 1 else " = ", end='')
    
    count -=1
f=factorial(n)

print(f)
# Usando for
'''n2 = int(input('Digite um número para saber o fatorial: '))
f2 = 1
for i in range(1, n2 + 1):
    f2 *= i
print(f'O resultado de {n2}! é {f2}')

# Usando math
from math import factorial
n3 = int(input('Digite um número para saber o fatorial: '))
print(f'O resultado de {n3}! é {factorial(n3)}')'''