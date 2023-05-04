def leiaint(n):
    while True:
        try:
            n = int(input(n))
            return n
        except ValueError:
            print("Valor inválido. Tente novamente!")



n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o numero {n}')