dados = {}
total = 0
dados['nome'] = input("Nome do Jogador: ")
numero_partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
dados['gols'] = []
for p in range(0, numero_partidas):
    partidas = int(input(f"Quantos gols na partida {p+1}? "))
    dados['gols'].append(partidas)

total = sum(dados['gols'])
dados['total'] = total

print('-='*40)
print(dados)
print('-='*40)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*40)
print(f"O jogador {dados['nome']} jogou {numero_partidas} partidas.")
for i, v in enumerate(dados['gols']):
    print(f"Na partida {i+1}, fez {v}.")
print(f"Foi um total de {dados['total']}.")
