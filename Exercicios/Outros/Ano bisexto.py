ano=(int(input("Qual ano você quer analisar?: ")))

if (ano%4) == 0 and (ano%100) !=0 or (ano%400) ==0:
     print(f"\033[34mO ano \033[33m{ano}\033[34m é bissexto\033[0m")     
else:
     print(f"\033[34mO ano \33[33m{ano}\033[34m não é bissexto\033[0m")