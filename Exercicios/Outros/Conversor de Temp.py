


temp=(input("A temperatura está em C° ou F°?: "))
#c=((temp - 32) * 5) / 9
#f=((9*c) / 5)+32



if temp.lower()==('c'):
        c=float(input("Digite a temperatura em C°: "))
        f=((9*c) / 5)+32
        c=((f - 32) * 5) / 9
        print(f"A temperatura de {c:.2f}°C para F° é: {f}F°")


elif temp.lower()==('f'):
        f=float(input("Digite a temperatura em F°: "))
        c=((f - 32) * 5) / 9
        f=((9*c) / 5)+32
        print(f"A temperatura de {f}°F para °C é: {c:.1f}C°")



