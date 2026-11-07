frase=str(input('digite sua frase')).strip().upper()
print('Na sua frase encontramos {} "As" '. format(frase.count('A')))
print(' Os A encontrados são : o primeiro está na posição {}° e o ultimo está na posição {}°'.format(frase.find('A')+1,frase.rfind('A')+1))
