n1=float(input('informe o velocidade :'))
if n1>80:
    print('Você será multado em {:.2f} reais por ter passado a {}km '.format((n1-80)*7.0,n1))
else:
    print ('você está dentro do limite de velocidade')
