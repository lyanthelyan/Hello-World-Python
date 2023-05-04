soma = 0
cont=0
for n in range(1, 500,2):
    if n % 3 == 0:
        cont = cont+1 #Se n % 3 for igual a zero, adiciona um no contador
        soma = n+soma
        
print(f"A soma de todos os {cont} valores é igual a {soma}")


