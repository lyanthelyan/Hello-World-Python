print('Veja com está seu IMC informando seu peso e altura abaixo. | Obs: Ao por a altura, use ponto em vez de virgula, EX: 1.85. Informe seu peso apenas em numeros inteiros EX: 65.')
peso = eval(input('Informe seu peso: '))
altu = eval(input('Informe sua altura: '))
x = peso/altu**2
print(f'Seu IMC é: {x}')
if x < 18:
  if x < 16:
    print('Você está abaixo do peso ideal, faça uma dieta e ganhe 16 kilos.')
  else: 
    if x < 18:
      print('Você está abaixo do peso ideal, faça uma dieta e ganhe 8 kilos.')
if x > 22.5:
  if x > 24.5:
    print('Você está acima do peso ideal, faça uma dieta e perda 16 kilos.')
  else:
    if x > 22.5:
      print('Você está acima do peso ideal, faça uma dieta e perda 8 kilos')
else: 
  if x > 18:
   print('Você está com o peso ideal! Continue assim.')