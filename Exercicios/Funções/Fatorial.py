from math import factorial

def fatorial(n, show=False):
    '''f=Fatorial do número
    count = aonde o número irá começar, no caso n
    show = se o show for true ele irá mostras o calculo, se não, irá apenas mostrar or resultado'''
    
    count=n
    print(f"{n}! = ", end='')
    f=factorial(n)
    if show:
        while count > 0:
            print(f"{count}", end='')
            if count > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
            count -= 1
        print(f)
    else:
        print(f)

fatorial(7, show=True)


#Guanabara

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        f *= c
    return f