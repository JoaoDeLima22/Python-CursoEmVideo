"""co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = (co**2 + ca**2)**(1/2)

print('A hipotenusa é {:.2f}'.format(hi))"""

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = hypot(co, ca)

print('A hipotenusa vai ser {:.2f}'.format(hi))
