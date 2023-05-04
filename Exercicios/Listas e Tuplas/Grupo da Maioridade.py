from datetime import date   
ano = date.today().year

anosmaiores=[]
anosmenores=[]

for a in range(1,8):
    anos=int((input(f"Em que ano a {a}º pessoa nasceu? ")))
    if ano-anos > 18:
        anosmaiores.append(anos)
    else:
        anosmenores.append(anos)    

print(f"Ao todo tivemos {len(anosmaiores)} pessoas maiores de idade")
print(f"E também tivemos {len(anosmenores)} pessoas menores de idade")


#atual = date.today().year
#totmaior=0
#totmenor=0
#for pess in range (1, 8):
#    nas=int(input(f'Em que ano a {pess}º pessoa nasceu? '))
##    idade=atual-nasc
#    if idade>=21:
#        totmaior+=1
#    else:
#        totmenor+=1
#print(f"Ao todo tivemos {totmaior} pessoas maiores de idade")
#print(f"E também tivemos {totmenor} pessoas menores de idade")



