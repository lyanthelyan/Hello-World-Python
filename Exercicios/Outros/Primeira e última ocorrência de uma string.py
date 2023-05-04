frase=input("Digite uma frase: ").strip().upper()

frase=frase.replace('Á','A').replace('Â','A').replace('À','A').replace('Â','A').replace('Ã','A')
print(f"A letra A aparece {frase.count('A')} vezes")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}")
print(f"A última letra A apareceu na posição {frase.rfind('A')+1}")