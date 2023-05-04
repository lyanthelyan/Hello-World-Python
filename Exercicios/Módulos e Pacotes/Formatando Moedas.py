#1- Versão
# import matematica


# preco_str = input("Digite o preço: R$")
# preco_str = preco_str.replace(",", ".") # substitui todas as vírgulas por pontos
# price = float(preco_str)
# print(f"A metade de {matematica.moeda(price)} é R${matematica.moeda(matematica.metade(price))}")
# print(f"O dobro de {matematica.moeda(price)} é R${matematica.moeda(matematica.dobro(price))}")
# print(f"Aumentando em 10%, nós temos R${matematica.moeda(matematica.porcentagem(price))}")

#2- Versão
import matematica


preco_str = input("Digite o preço: R$")
preco_str = preco_str.replace(",", ".") # substitui todas as vírgulas por pontos
price = float(preco_str)
print(f"A metade de {matematica.moeda(price)} é {matematica.metade(price, True)}")
print(f"O dobro de {matematica.moeda(price)} é {matematica.dobro(price, True)}")
print(f"Aumentando em 10%, nós temos {matematica.porcentagem(price, True)}")