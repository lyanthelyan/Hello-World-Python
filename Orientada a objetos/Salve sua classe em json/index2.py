from index import caminho_arquivo
import json
with open (caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)
    novo_dados = json.dumps(dados, indent=2)
    print(novo_dados)