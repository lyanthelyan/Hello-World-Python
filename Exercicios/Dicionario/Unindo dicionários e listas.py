dados = []
total = 0
mulheres = []
#------------------------------------------------------------------
while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ")
    
    pessoa['sexo'] = input("Sexo: [M/F] ").upper()
    while pessoa['sexo'] not in ['M', 'F']:
        print("Erro! Por favor, digite apenas M ou F.")
        pessoa['sexo'] = input("Sexo: [M/F] ").upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
 #--------------------------------------------------------------       
    while True:
        try:
            pessoa['idade'] = int(input("Idade: "))
            total += pessoa['idade']
            break
        except ValueError:
            print("Erro. Digite um valor inteiro para a idade.")
    dados.append(pessoa)

#-----------------------------------------------------------------------    
    continuar = input("Quer Continuar? [S/N] ").strip().upper()
    while continuar not in ['S', 'N']:
        print("Erro! Por favor, digite apenas S ou N.")
        continuar = input("Quer Continuar? [S/N] ").strip().upper()

    if continuar == 'N':
        break
#----------------------------------------------------------------------------
media = total / len(dados)

print('-='*50)
print(f"(A) Ao todo temos {len(dados)} pessoas cadastradas.")
print(f"(B) a média de idade é de {media:.2f} anos.")
if len(mulheres) == 0:
    print("(C) Não houve mulheres cadastradas.")
else:
    print("(C) As mulheres cadastradas foram " + ", ".join(mulheres)+".")
print("(D) Lista de pessaos acima de média: ")
for pessoa in dados:
    if pessoa['idade'] >= 18:
        #print('     ')
        for k, v in pessoa.items():
            print(f'  {k} = {v}; ',end='')
        print()
print('-='*50)
