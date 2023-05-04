valor=int(input("Valor da casa: R$"))
salario=int(input("Salário do comprador: R$"))
anos=int(input("Quantos anos de ficanciamento? "))
presta=valor/(anos*12)

print(f"Para pagar uma casa de valor R${valor} em {anos} anos, a prestação será de R${presta:.2f}!")
if salario <= presta * 2:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo APROVADO!")



