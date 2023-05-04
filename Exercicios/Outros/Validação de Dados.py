

sexo=input("Informe seu sexo[M/F]: ").upper().strip()
while sexo != 'M' and sexo != 'F': #'F'!=sexo!='M'
    sexo=input("Dados inválidos. Por favor, informe seu sexo: ").upper().strip()
print(f'Sexo {sexo} registrado com sucesso')
