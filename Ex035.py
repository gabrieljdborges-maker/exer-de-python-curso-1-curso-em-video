a=float(input('Digite o valor do primeiro lado A :'))
b=float(input('Digite o valor do segundo lado B :'))
c=float(input('Digite o valor do terceiro lado C :'))
if a+b>c:
    if b+c>a:
        if a+c>b:
            print('Temos um triangulo!!!! :)')
else :
    print('Com essas medidas não conseguimos formar um triangulo :( ')