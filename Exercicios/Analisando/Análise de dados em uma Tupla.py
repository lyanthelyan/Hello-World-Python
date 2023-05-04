num=(int(input("Digite um número: ")),
     int(input("Digite outro número: ")),
     int(input("Digite mais um número: ")),
     int(input("Ddigite o último número: ")))
#------------------------------------------------------------
num_str = ', '.join(str(n)for n in num)
print(f"Você digitou os valores {num_str}.")
print(f"O valor 9 apareceu {num.count(9)} vezes.")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)}º posição.")
else:
    print(f"O valor 3 não se encontra.")
#--------------------------------------------------------------
pares=[]
for n in num:
    if n % 2 ==0:
        pares.append(n)
pares_str = ', '.join(str(p) for p in pares)
print(f"Os valores pares digitados foram {pares_str}.")

#10 linhas 
'''c=0
par=tupla=()
while c<4:
    x=int(input(f"{c+1}- Digite um valor: "))
    tupla+=x, # Coloque virgula para atribuir um item à tupla
    c+=1
    if x % 2 == 0:
        par+=x,
print(f"O número 9 apareceu {tupla.count(9)} vez(es)")
print(f"O número 3 apreceu primeiro na posição {tupla.index(3)+1}")
print(f"Os números pares foram: {par}")'''