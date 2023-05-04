def notas(*n, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    n: uma ou mais notas (aceita várias)
    situação: (opcional), indica se deve ou não mostrar a situação do aluno.
    return: dicionário com várias informações sobre a situação da turma.
    """
    
    
    notas = {}
    soma = sum(n)
    notas['total']= len(n)
    notas['maior']= max(n)
    notas['menor']= min(n)
    notas['média']= soma / len(n)
    if sit == True:
        if notas['média'] >= 7:
            notas['situação'] = 'Bom'
        elif 6 <= notas['média'] < 7:
            notas['situação'] = 'Moderável'
        else:
            notas['situação'] = 'Ruim'
    return notas


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)