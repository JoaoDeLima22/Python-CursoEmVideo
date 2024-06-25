import math
angulo = float(input('Digite o valor do angulo: '))
seno= math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tan= math.tan(math.radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('o angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('o angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))
