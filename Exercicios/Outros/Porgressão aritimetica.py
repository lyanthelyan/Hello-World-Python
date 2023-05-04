#10 TERMOS DE UMA PA


'''primeiro_termo=int(input("Primeiro termo: "))
razao=int(input("Razão: "))
decimo = primeiro_termo + (10-1) *razao
for pa in range(primeiro_termo, decimo+razao, razao):
    print(f"{pa}", end='→')
print('Acabou!')'''''



print('Gerador de PA')
print('-='*10)
primeiro = int(input("Primeiro termo: "))
razao=int(input("Razão da PA: "))
termo = primeiro
cont=1

while cont <= 10:
    
    
    print(f"{termo} -> ",end='')
    termo+=razao
    cont+=1
print('Fim')