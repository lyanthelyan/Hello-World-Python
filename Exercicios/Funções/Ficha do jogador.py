def ficha(n='desconhecido',g=''):
    if n != '':
        n = n
    else: 
        n ='desconhecido'
    
    try:
        if g != '': 
            g = int(g)
        else:
            g = 0
    except ValueError:
        g = 0
    
    print(f"O jogador {n} fez {g} gol(s) no campeonato.")

n = input("Nome do jogador: ").strip()
g = input("Número de Gols: ").strip()

ficha(n, g)

