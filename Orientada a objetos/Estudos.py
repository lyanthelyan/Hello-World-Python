# class Pessoa:
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade


# p1 = Pessoa('Luiz', 'Otávio', 18)
# # p1.nome = 'Luiz'
# # p1.sobrenome = 'Otávio'

# p2 = Pessoa('Maria', 'Joana', 20)
# # p2.nome = 'Maria'
# # p2.sobrenome = 'Joana'

# print(p1.nome)
# print(p1.sobrenome)
# print(p1.idade)

# print(p2.nome)
# print(p2.sobrenome)

class Carro():
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor


c1 = Carro('Chevrolet', 'Corsa', 'Vermelho')
c2 = Carro('Fiat', 'Siena', 'Branca')
c3 = Carro('Hyundai', 'HB20', 'Branca')

print(f'O carro da marca {c1.marca} e do modelo {c1.modelo} tem a cor {c1.cor}')
print(f'O carro da marca {c2.marca} e do modelo {c2.modelo} tem a cor {c2.cor}')
print(f'O carro da marca {c3.marca} e do modelo {c3.modelo} tem a cor {c3.cor}')