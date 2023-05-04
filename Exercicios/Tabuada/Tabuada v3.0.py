from colorama import init, Fore, Style
init()

while True:
    print(Fore.LIGHTMAGENTA_EX+'-=-'*20)
    n = int(input(Fore.YELLOW + "Quer ver a tabuada de qual valor? "+Fore.GREEN))
    
    if n < 0:
        print(Fore.RED+f'Programa encerrado, Volte novamente.')
        break
    count = 0
    while count <10:
        count+=1
        tabuada=n*count
        
        print(Fore.BLUE+f'{n} x {count} = '+Fore.GREEN+f'{tabuada}')






        
    


    