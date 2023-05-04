print('-'*38)
print('         Loja Super Baratão')
print('-'*38)
#----------------------------------------
totcompras=0
produtomais1000=0
maisbarato=0
count=0
produtobarato=''
#-----------------------------------------
while True:
    produto=input("Nome do Produto: ").strip()
    try:
        preço=float(input("Preço: R$"))
        totcompras+=preço
        count+=1    
    except ValueError:
        print("Entrada inválida. Tente Novamente!")
        continue      
#------------------------------------      
    if preço >= 1000:
        count+=1
        produtomais1000+=1
#---------------------------------    
    if count == 1:
        produtobarato = produto
        maisbarato = preço
    else:
        if preço < maisbarato:
            maisbarato = preço
            produtobarato = produto
#-------------------------------------    
    continuar=' '
    while continuar not in 'SN':
        continuar=input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar == 'N':
        print("-"*12+"Fim do Programa"+"-"*12)
        break
    if continuar == 'S':
        continue
#----------------------------------------
print(f"O total da compra foi R${totcompras:.2f}")
print(f"Temos {produtomais1000} produtos custandos mais de R$1000.00")
print(f"O produto mais barato foi {produtobarato} e o seu preço foi R${maisbarato}")