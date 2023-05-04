#1-Dada uma lista de números, crie uma nova lista contendo apenas os números pares.
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in original if num % 2 == 0]

#2-Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras com mais de 5 letras.
palavras = ["apple", "banana", "grapefruit", "pear", "kiwi", "orange"]
maiores_5 = [word for word in palavras if len(word) > 5]

#3-Dada uma lista de números, crie uma nova lista contendo o quadrado de cada número.
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [num ** 2 for num in original]

#4-Dada uma lista de nomes, crie uma nova lista contendo apenas os nomes que começam com a letra "A".
nomes = ["Ana", "Beatriz", "Carla", "Daniel", "Elaine", "Felipe", "Adriana"]
a_names = [name for name in nomes if name.startswith("A")]

#5-Dada uma lista de números, crie uma nova lista contendo apenas os números ímpares maiores que 5.
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares_maiores_5 = [num for num in original if num % 2 != 0 and num > 5]

#6-Dada uma lista de nomes, crie uma nova lista contendo os mesmos nomes, mas em letras minúsculas.
nomes = ["Ana", "Beatriz", "Carla", "Daniel", "Elaine", "Felipe", "Adriana"]
lower_names = [name.lower() for name in nomes]

#7-Dada uma lista de números, crie uma nova lista contendo apenas os números que são divisíveis por 3 e 5.
original = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
divisiveis_3_5 = [num for num in original if num % 3 == 0 and num % 5 == 0]
