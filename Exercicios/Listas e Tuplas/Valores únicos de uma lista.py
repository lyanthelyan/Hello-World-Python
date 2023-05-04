duplicado=''
lista=[]
while True:
    try:
        valor=int(input("Digite um número: "))        
    except ValueError:
        print("Valor inválido, não é um número")
        continue
    if valor not in lista:
        print("Valor adicionado!")
        lista.append(valor)
    else:
        print("Valor duplicado não vou adicionar!")
             
    
    continuar=input("Quer continuar? [S/N] ").strip().upper()

#----------------------------------------------------------------------------------  
    if continuar == 'N':
        break
    if continuar == 'S':
        continue
    while 'N'!=continuar!='S':
        continuar=input("Valor inválido. Quer continuar? [S/N] ").strip().upper()
 #---------------------------------------------------------------------------------     
        
print("Você digitou os valores ", end='')
lista_crescente = sorted(lista)
print(*lista_crescente)