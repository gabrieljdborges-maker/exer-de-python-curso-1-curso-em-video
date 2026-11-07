from  random import randint
from time import sleep
num=int(randint(0,5))
print('-=-=-='*20)
n1=int(input('escolhi um numero entre 0 e 5, Qual é ?? '))
print('-=-=-='*20)
print ('Processando .......')
sleep(4)
if n1==num:
    print('Muito bem !!! você acertou !!!!')
else:
    print ('Numero errado, o numero que escolhi é o {} tente novamente'.format(num))
print('GG')