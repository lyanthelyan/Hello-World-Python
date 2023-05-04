
maior18=0
homens=0
mulheresmenos20=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    try:
        idade=int(input("Idade: "))
    except ValueError:
        print("Entrada inválida. Tente novamente!")
        continue    
    sexo=input("Sexo: [M/F] ").strip().upper()
    if sexo != 'M' and sexo != 'F':
        print("Entrada inválida.Tente novamente!")
        continue
    if idade >= 18:
       maior18+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        mulheresmenos20+=1
    
    continuar=' '
    while continuar not in 'SN':
        continuar=input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print(f"Total de pessoas maiores de idade: {maior18}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheresmenos20} mulheres com menos de 20 anos")
