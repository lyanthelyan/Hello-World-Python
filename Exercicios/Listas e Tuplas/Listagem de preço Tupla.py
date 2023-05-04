listagem=('Lápis',1.75,
          'Borracha',2,
          'Caderno',15.90,
          'Estojo',25,
          'Transferidor',4.20,
          'Compasso',9.99,
          'Mochila',120.32,
          'Canetas',22.3,
          'Livro',34.9)
print('-'*40)
print(f"{'LISTAGEM DE PREÇO':^40}")
print('-'*40)
for posição in range(0,len(listagem)):   
    if posição % 2 ==0:
        print(f"{listagem[posição]:.<30}",end='')
    else:
        print(f"R${listagem[posição]:>7.2f}")
print('-'*40)
'''tabela = ('Caneta', 1.0, 'Lapis', 5.0, 'Borracha', 0.5, 'Caderno', 20.0, 'Fichário', 29.99)
 titulo = 'LISTAGEM DE PREÇOS'
 print("--" * 20)                # CABEÇALHO
 print(f"{titulo: ^40}")     #
 print("--" * 20)                #
 for items in tabela:         
    if type(items) == str:
          print(f"{items:.<30}", end="")
    if type(items) == float:
        print(f"R${items: >7.2f}")
 print("--" * 20)

'''