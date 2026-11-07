import math
a=float(input('informe o valor do angulo '))
print('O valor do sen do angulo {} é {:.2f}'.format(a,math.sin(math.radians(a))))
print('O valor do cos do angulo {} é {:.2f}'.format(a,math.cos(math.radians(a))))
print('O valor da tag do angulo {} é {:.2f}'.format(a,math.tan(math.radians(a))))
# quando utlizarmos math para angulo sempre utilizar o conversor para radiands