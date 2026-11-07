a=float(input('Informe o valor do primeiro numero'))
b=float(input('Informe o valor do priemiro numero'))
c=float(input('Informe o valor do terceiro numero'))
if a>b and a>c:
    print('O maior numero é o {}'.format(a))
if b>a and b>c:
    print('O maior numero é o {}'.format(b))
if c>a and c>b:
    print('O maior numero é o {}'.format(c))
if a==b and c==b and a==c:
    print ('Os valores são iguais')
