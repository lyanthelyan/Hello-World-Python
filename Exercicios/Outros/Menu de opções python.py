from time import sleep
primeiro_valor=int(input("Primeiro valor: "))
segundo_valor=int(input("Segundo valor: "))
sair = False
while not sair:
    print(      "[ 1 ] Somar\n"
            "[ 2 ] Multiplicar\n"
            "[ 3 ] Maior\n"
            "[ 4 ] Novos Números\n"
            "[ 5 ] Sair do Programa")
    try:
        op = int(input("Qual a sua opção: "))
    except ValueError:
        print("Entrada inválida, tente novamente.")
        continue
   
    
    if op != 1 and op!=2 and op!=3 and op!=4 and op!=5:
        print("Entrada inválida, Tente novamente!")
    elif op == 1:
        resultado = primeiro_valor+segundo_valor
        print(f"A soma dos valores é {resultado}")
    elif op == 2:
        resultado=primeiro_valor*segundo_valor
        print(f"A multiplicação dos valores é {resultado}")
    elif op == 3:
        lista=[primeiro_valor, segundo_valor]
        print(f"O maior valor das opções é o {max(lista)}")
    elif op == 4:
        primeiro_valor=int(input("Primeiro valor: "))
        segundo_valor=int(input("Segundo valor: "))
    elif op == 5:
        print("Finalizando...")
        sleep(1.5)
        sair=True
    
        
        



