numero=int (input('Digite o numero'))
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10
print('Seu numero tem {} unidades'.format(u))
print('Seu numero tem {} dezenas'.format(d))
print('Seu numero tem {} centenas'.format(c))
print('Seu numero tem {} milhares'.format(m))