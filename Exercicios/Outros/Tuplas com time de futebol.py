times = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético','Botafogo','Atlético-Pr',
         'Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória','Coritiba','Avaí','Ponte Preta')
def tupla():
    print('-='*15)
    print(f'\033[1mLista de times do Brasileirão:\033[0m {times}')
    print('-='*15)    
    print(f"\033[1mOs 5 primeiros sãos:\033[0m {times[:5]}")
    print('-='*15)
    print(f"\033[1mOs 4 últimos são:\033[0m {times[-4:]}")  
    print('-='*15)
    print(f"\033[1mTimes em ordem alfabética:\033[0m {sorted(times)}") 
    print('-='*15)
    print(f'\033[1mA Chapecoense está na {times.index("Chapecoense")}º posição\033[0m')
    print('-='*15)
tupla()