num=int(input("Digite um número [999 para parar]: "))
count=0
soma= 0

while not num==999:
    soma+=num
    count+=1
    num=int(input("Digite um número [999 para parar]: "))
print(f'Você digitou {count} números e a soma entre eles foi {soma}.') 