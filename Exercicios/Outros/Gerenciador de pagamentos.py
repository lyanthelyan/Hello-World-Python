print('============= LOJA MACACO =============')
preço=float(input("Preço das compras: R$"))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')



opc=int(input("Qual a opção? "))
desconto=preço-(preço*10/100)
#juros=preço+(preço*1/100)

if opc==1:
    desconto=preço-(preço*10/100)
    print(f"Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.")
elif opc==2:
    desconto=preço-(preço*5/100)
    print(f"Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.")
elif opc ==3:
    #parcela=int(input('Quantas parcelas? '))
    juros=preço+(preço*30/100)
    parcela2x=preço/2
    print(f"Sua compra será parcelada em 2x de R${parcela2x:.2f}")
    print(f"Sua compra de R${preço:.2f} vai custar R${preço:.2f} no final.")
elif opc ==4:
    parcela=int(input('Quantas parcelas? '))
    juros=preço+(preço*20/100)
    parcela3x=juros/parcela
    print(f"Sua compra será parcelada em {parcela}x de R${parcela3x:.2f} COM JUROS")
    print(f"Sua compra de R${preço:.2f} vai custar R${juros:.2f} no final.")
elif opc !=(1,2,3,4):
    print("Opção Inválida, tente novamente!")

