# def terreno():
#     print(f"{'Controle de Terrenos':^50}")
#     print('-'*50)
#     largura = float(input("Largura (M): "))
#     comprimento = float(input("Comprimento (M): "))
#     print(f"A área de um terreno {largura} x {comprimento} é de {largura*comprimento}m².")

# terreno()

# def terreno(largura, comprimento):
#     print(f"{'Controle de Terrenos':^50}")
#     print('-'*50)
#     print(f"Largura (M): {largura}")
#     print(f"Comprimento (M): {comprimento}")
#     print(f"A área de um terreno {largura} x {comprimento} é de {largura*comprimento}m².")

# terreno(10,25.5)

#GUANABARA
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


print( 'Controle de Terrenos')
print('-'*20)
l = float(input("Largura (M): "))
c = float(input('Comprimento (M): '))
área(l, c)