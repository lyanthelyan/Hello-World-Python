#lst=[]  #lista vazia
#for c in range(1, 6):
#    peso=float(input('Peso da {}ª pessoa: '.format(c)))
#    lst+=[peso]   #adc os valores de peso na lista
#print('')
#print('O Maior peso foi:', max(lst))  #maximo valor da lista
#print('O Menor peso foi:', min(lst))  #minimo valor da lista

#pesos = [float(input(f'Peso da {a}º pessoa: ')) for a in range(1, 6)]
#print(f'O maior peso foi de {max(pesos)}Kg\n'
#      f'O menor foi de {min(pesos)}Kg!')


#lista= []
#for c in range (1,6):
#    lista.append(float(input (f'Qual o peso da {c}ª pessoa?')))
#print ('O maior peso é', max(lista))
#print ('O menor peso é', min(lista))

maior_peso = 0
menor_peso = 0
for todas_as_pessoas in range(1, 6):
    peso_inserido = float(input('Insíra o peso da {}ª pessoa: '.format(todas_as_pessoas)))
    if todas_as_pessoas == 1:
        maior_peso = peso_inserido
        menor_peso = peso_inserido
    else:
        if peso_inserido > maior_peso:
            maior_peso = peso_inserido
        if peso_inserido < menor_peso:
            menor_peso = peso_inserido
print('O maior peso é de {} e o menor peso é de {}'.format(maior_peso, menor_peso))