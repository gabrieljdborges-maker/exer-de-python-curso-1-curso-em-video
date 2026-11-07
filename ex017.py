import math
x1=float(input('informe o valor do cateto adjacente '))
x2=float(input('informe o valor do cateto oposto '))
h=pow(pow(x1,2)+pow(x2,2),1/2)
print('O valor da hipotenusa é {}'.format(math.floor(h)))
## temos uma segunda forma para fazer esse programa
x3=float(input('informe o valor do cateto adjacente '))
x4=float(input('informe o valor do cateto oposto '))
print('o valor da Hipotenusa é {:.2f}'.format(math.hypot(x3,x4)))
