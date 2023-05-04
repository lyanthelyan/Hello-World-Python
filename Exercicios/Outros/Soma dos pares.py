#n1=(int(input("Primeiro numero: ")))
#n2=(int(input("Segundo numero: ")))
#n3=(int(input("Terceiro numero: ")))
#n4=(int(input("Quarto numero: ")))
#n5=(int(input("Quinto numero: ")))
#n6=(int(input("Sexto numero: ")))


#soma=0
#for s in (n1,n2,n3,n4,n5,n6):
#    if s % 2 == 0:
#        soma=soma+s
#print(f"A soma dos números é igual a {soma}")

soma = 0
conti = 0
contp= 0
for c in range(1, 7):
    num=int(input(f"Digite o {c} valor: "))
    if num % 2==0:
        soma = soma+num
        contp = contp+1
    conti=conti+1

print(f"Você informou {conti} valores e os pares foram {contp} números, e a soma dos deles foram {soma}")





    
