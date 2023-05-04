from datetime import date

ano=int(input("Ano de nascimento: "))
year = date.today().year
idade = year-ano


print(f"Quem nasceu em {ano} tem {idade} anos em {year}")
if idade == 18:
    print("Você precisa se alistar imediatamente! ")
elif idade < 18:
    saldo=abs(18-idade)
    print(f"Ainda faltam {saldo} anos para o alistamento")
    print(f"Seu alistamento será em {saldo+year}")

elif idade > 18:
    saldo=abs(18-idade)
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    print(f"Seu alistamento foi em {year-saldo}")