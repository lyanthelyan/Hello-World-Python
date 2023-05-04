from datetime import date

current_year = date.today().year
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int((input('Ano de Nascimento: ')))
cadastro['ctps'] = str(input('Carteira de Trabalho (0 não tem): '))

#cadastro['idade'] =current_year - cadastro['idade']


if cadastro['ctps'] == str(0):
        cadastro['idade'] =current_year - cadastro['idade']
        print('-='*50)
        for v, k in cadastro.items():
            print(f'- {v} tem o valor {k}')
        
elif cadastro['ctps'] != str(0):
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = ((cadastro['contratação'] - cadastro['idade']) + 35)           
    cadastro['idade'] =current_year - cadastro['idade']
    print('-='*50)
    for v, k in cadastro.items():
        print(f'- {v} tem o valor {k}')
            

