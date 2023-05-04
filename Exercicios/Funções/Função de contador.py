from time import sleep


def contador(i, f, p):
    if p < 0:
        p = abs(p)
    print('\033[1;31m-=-\033[m' * 15)
    print(f'Contando de {i} até {f} de {p} em {p}:')
    print('\033[1;31m-=-\033[m' * 15)
    if i < f:
        cont = i
        while cont <= f:
            print(f'→ {cont} ', end='')
            sleep(0.5)
            cont += p
        print()
    if i > f:
        cont = i
        while cont >= f:
            print(f'→ {cont} ', end='')
            sleep(0.5)
            cont -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)

#Programa Principal
print('\033[1;31m-=-\033[m' * 15)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('\033[1;31m-=-\033[m' * 15)

contador(inicio, fim, passo)