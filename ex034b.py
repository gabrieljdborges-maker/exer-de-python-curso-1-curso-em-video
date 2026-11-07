salario=(float(input('Digite o seu salario ? ')))
if salario<=1250:
    novo=salario+(salario*15/100)
else:
    novo=salario+(salario*10/100)
print ('Seu salario era R${:.2f} agora é R${:.2f}'.format(salario,novo))
