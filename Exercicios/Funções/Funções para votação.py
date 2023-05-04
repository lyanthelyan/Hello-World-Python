from datetime import date
def voto(ano):
    year = date.today().year
    idade = year - ano    
    if idade >= 18:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO!")
    elif idade<18 and idade >=16:
        print(f"Com {idade} anos: VOTO OPCIONAL!")
    elif idade <16:
        print(f"Com {idade} anos: NÃO VOTA.")
    return idade


voto(int(input("Em que ano você nasceu? ")))