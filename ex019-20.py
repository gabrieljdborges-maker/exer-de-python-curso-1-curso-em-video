from random import shuffle , choice
a1=input('informe o nome do aluno ')
a2=input ('informe o nome do aluno 2 ')
a3=input ('informe o nome do alino 3 ')
a4=input (' Informe o nome do aluno 4 ')
lista=[a1,a2,a3,a4]
print(' O aluno escolhido para limpar o quadro é {} '.format(choice(lista)))
shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))
