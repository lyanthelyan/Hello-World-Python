num=int(input("Informe um número: "))

u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10


print(f"Analisando o número {num}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")


#Divisão: 1234 / 10 = 123,4
#Divisão inteira: 1234 //10 = 123
#Módulo: 1234 % 10 = 4
#Pra ele descobrir a centena ele faz isso:
#Faz a divisão inteira por 100: 1234 // 100 = 12
#Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
#Ou seja, a centena é 2.
