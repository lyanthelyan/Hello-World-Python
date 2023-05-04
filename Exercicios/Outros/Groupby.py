from itertools import groupby
#Exercício 1: Agrupar por idade
#Dado o seguinte dicionário de pessoas e suas idades:

pessoas = [
    {'nome': 'Ana', 'idade': 23},
    {'nome': 'Bruno', 'idade': 18},
    {'nome': 'Carlos', 'idade': 23},
    {'nome': 'Daniel', 'idade': 25},
    {'nome': 'Eva', 'idade': 18},
    {'nome': 'Fernando', 'idade': 25},
    {'nome': 'Gabriel', 'idade': 23},
    {'nome': 'Isabela', 'idade': 20},
    {'nome': 'Julia', 'idade': 20},
    {'nome': 'Larissa', 'idade': 18}
]

pessoas_sorted = sorted(pessoas, key = lambda x: x['idade'])
group = groupby(pessoas_sorted, key = lambda x: x['idade'])

# for g, k in group:
#     print(f'Grupo: {g} anos de idade , Pessoas:{list(k)}')



produtos = [
    {'nome': 'Arroz', 'preco': 12.5},
    {'nome': 'Feijão', 'preco': 8.99},
    {'nome': 'Macarrão', 'preco': 4.5},
    {'nome': 'Leite', 'preco': 3.29},
    {'nome': 'Carne', 'preco': 29.99},
    {'nome': 'Peixe', 'preco': 17.99},
    {'nome': 'Tomate', 'preco': 2.99},
    {'nome': 'Cebola', 'preco': 1.99},
    {'nome': 'Alho', 'preco': 5.5}
]

produtos_sorted = sorted(produtos, key = lambda x: x['preco'])
group = groupby(produtos_sorted, key= lambda x: x['preco'])

# for g, k in group:
#     print(f'Preço de {g}, Produtos:{list(k)}')

#Agrupar por tamanho de palavra

palavras = {'abacate', 'banana', 'caju', 'damasco', 'figo', 'groselha', 'jabuticaba'}

palavras_sorted = sorted(palavras, key =  lambda x: len(x), reverse=True)
group = groupby(palavras_sorted, key = lambda x: len(x))

for g, k in group:
    palavras = ', '.join(k).capitalize()
    print(f'{g} palavras: {palavras}')