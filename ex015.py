d=int(input('Por quantos dias o carro foi alugado ?'))
k=int(input('Quantos KMs foram percorridos ?'))
a=60*d+k*0.15
print('O valor a ser pago do Aluguel é de R${:.2f}'.format(a))
