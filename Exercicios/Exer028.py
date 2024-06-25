import random

N1= random.randint(0,5)

N2 = int(input('Tente um numero de 0 a 5:'))
if N1 == N2:
    print('muito bem voce acertou')
else:
    print('Você errou o numero sorteado foi {}'.format(N1))