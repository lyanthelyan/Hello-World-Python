caminho_arquivo = "C:\\Users\\T-GAMER\\Documents\\Workspace\\Hello World Python\\Projeto JSON\\"
caminho_arquivo += 'aula116.txt'
# arquivo = open(caminho_arquivo, 'w')
# arquivo.write('Oi')
# arquivo.close()

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Ola Mundo')