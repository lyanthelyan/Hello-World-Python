aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situação']='Aprovado'
elif 5<=aluno['media'] <7:
    aluno['situação']='Recuperação'
print('-='*20)
for k,v in aluno.items():
    print(f"O {k} é igual a {v}")
