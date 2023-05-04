def metade(n=0, format=False):
    res =  n / 2
    return res if format is False else moeda(res)

def dobro(n=0, format=False):
    res =  n * 2
    return res if format is False else moeda(res)
def porcentagem(n=0, format=False):
    res = n * 0.1
    return n + res if format is False else moeda(res)
def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
def porcentagem2(n=0, a=0,  format=False):
    res = n * (a / 100) + n
    return n + res if format is False else moeda(res)
def porcentagemreduzida(n=0, r=0,  format=False):
    res = n - (n * (r / 100))
    return n - res if format is False else moeda(res)

def resumo(n=0,a=0,r=0):
    print('-'*36)
    print(f'{"RESUMO DO VALOR".center(36)}')
    print('-'*36)
    print(f"Preço analisado...........{moeda(n)}")
    print(f"Dobro do preço............{dobro(n, True)}")
    print(f"Metade do preço...........{metade(n, True)}")
    print(f"{a}% de aumento............{porcentagem2(n,a, True)}")
    print(f"{r}% de redução............{porcentagemreduzida(n,r, True)}")
    print('-'*36)



# #def moedaporcentagem(n):
# #    def porcentagem(n=0):
# #        p = n *0.1
# #        return n+ p
#  #   def moeda (preço = 0, moeda = 'R$'):
# #        return f'{moeda}{preço:>.2f}'.replace('.',',')
# #    valorpocentagem = porcentagem(n)
# #    return moeda(valorpocentagem)

# #def moedametade(n):
#     def moeda(preço = 0, moeda = 'R$'):
#         return f'{moeda}{preço:>.2f}'.replace('.',',')
#     def metade(n=0):
#         return n / 2
#     valor_metade = metade(n)
#     return moeda(valor_metade)

# #def moedadobro(n):
#     def moeda(preço = 0, moeda = 'R$'):
#         return f'{moeda}{preço:>.2f}'.replace('.',',')
#     def dobro(n=0):
#         return n * 2
#     valor_dobrado = dobro(n)
#     return moeda(valor_dobrado)