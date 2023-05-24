import json
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = "C:\\Users\\T-GAMER\\Documents\\Workspace\\Hello World Python\\Projeto JSON\\"
caminho_arquivo += 'aula116.txt'
# arquivo = open(caminho_arquivo, 'w')
# arquivo.write('Oi')
# arquivo.close()
# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Ola Mundo\n')
#     arquivo.writelines(
#         ('Oi\n', 'Teste de Linha\n', 'Terceira linha\n')
#     )
#     arquivo.write('Atenção\n')
#     arquivo.seek(0,0)
#     print(arquivo.readline())

# with open ("C:\\Users\\T-GAMER\\Documents\\Workspace\\Hello World Python\\Projeto JSON\\states.json") as f:
#     data = json.load(f)

# new_string = json.dumps(data, indent=2) #Jeito De ver o arquivo json mais organizado
# print(new_string)


# for state in data['states']:  # Caminhar no arquivo json, igual um dicionario
#     del state['area_codes']
#     print(state['area_codes'])
    

from urllib.request import urlopen

with urlopen('https://openexchangerates.org/api/currencies.json') as response:
    source = response.read()

data = json.loads(source)
print(json.dumps(data, indent=2))

# for s, p in data.items():
#     print(f"Moeda : {s}\nPaís : {p}")
#     print()


