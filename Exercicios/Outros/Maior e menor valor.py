n1=float(input("Primeiro valor: "))
n2=float(input("Segundo valor: "))
n3=float(input("Terceiro valor: "))



if n1>n2 and n1>n3:
    print(f"O maior valor é {n1}")
elif n2>n1 and n2>n3:
    print(f"O maior valor é {n2}")
elif n3>n1 and n3>n2:
    print(f"O maior valor é {n3}")

if n1<n2 and n1<n3:
    print(f"O menor valor é {n1}")
elif n2<n1 and n2<n3:
    print(f"O menor valor é {n2}")
elif n3<n1 and n3<n2:
    print(f"O menor valor é {n3}")
#-------------------------------------------------------------------------

#a=int(input("Primeiro valor: "))
#b=int(input("Segundo valor: "))
#c=int(input("Terceiro valor: "))

#maior = a
#if b>a and b>c:
    #maior = b
#if c>a and c>b:
  #  maior = c

#menor=a
#if b<a and b<c:
    #menor = b
#f c<a and c<b:
    #menor=c
#print(f"O maior valor é {maior}")
#print(f"O menor valor é {menor}")
#-------------------------------------------------------------------------
primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print(f'O maior valor digitado foi {max(numeros)}')
print(f'O menor numero digitado foi {min(numeros)}')


