import random

numeros=(random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10)), (random.randint(1,10))

print(f"Os valores sorteados foram ",end='')
for n in numeros:
    print(f"{n} ",end='')

print(f"\nO maior valor foi {max(numeros)}")
print(f"O menor valor foi {min(numeros)}")