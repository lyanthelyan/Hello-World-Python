import json
caminho_arquivo = 'C:\\Users\\T-GAMER\\Documents\\Workspace\\Hello World Python\\Orientada a objetos\\Salve sua classe em json\\dados.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

p1 = Pessoa('João', 22)
p2 = Pessoa('Maria', 14)
dados = vars(p1), vars(p2)
# Salvando os dados no arquivo JSON

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)



