

import random
import sys

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))


    contador_regressivo= 10

    resultado = 0


    for digito in nove_digitos:
        resultado += (int(digito) * contador_regressivo)
        contador_regressivo += -1

    digito_1 = (resultado*10) % 11
    digito_1 = digito_1 if digito_1 <=9 else 0
    #print(digito_1)
    #---------------------------------------------------------------------
    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2=11

    resultado_digito_2=0
    for digito in dez_digitos:
        resultado_digito_2+=(int(digito) * contador_regressivo_2)
        contador_regressivo_2 -=1
    digito_2 = (resultado_digito_2*10)%11
    digito_2= digito_2 if digito_2 <= 9 else 0


    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    print(cpf_gerado_pelo_calculo)