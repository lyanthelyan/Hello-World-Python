from time import sleep
colorst={'blue':'\033[34m',
        'red':'\033[31m',
        'green':'\033[32m',
        'yellow':'\033[33m',
        'black':'\033[30m',
        'white':'\033[97m',
        'cyan':'\033[36m',
        'grey':'\033[37m',
        'magenta':'\033[35m',
        'none':'\033[0m'}

nome=input("Digite seu nome completo: ").strip()
print(f"{colorst['red']}Analisando seu nome...{colorst['none']}")
sleep(2)
print(f"\033[34mSeu nome em \033[1;32mMAIÚSCULAS\033[0m \033[34mé:\033[0m \033[4;36m{nome.upper()}\033[0m")
sleep(1)
print(f"\033[34mSeu nome em \033[1;32mMINÚSCULAS\033[m \033[34mé: \033[0m\033[4;36m{nome.lower()}\033[0m")
sleep(1)
print(f"\033[34mSeu nome tem ao todo \033[33m{len(nome)-nome.count(' ')} \033[34mletras\033[0m")
sleep(1)
primeiro_nome=nome.split() # Split irá transformar o nome em listas, assim fica mais facil de lozalicar [0]



print(f"\033[34mSeu primeiro nome é \033[4;36m{primeiro_nome[0]}\033[0m \033[34me ele tem \033[33m{len(primeiro_nome[0])} \033[34mletras\033[0m")

