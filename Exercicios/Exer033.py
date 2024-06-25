a = float(input('Digite o primeiro'))
b = float(input('Digite o segundo'))
c = float(input('Digite o terceiro'))
maior = a
if b >a and b > c:
    maior = b
if c >a and c > b:
    maior=c

menor=a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O maior valor foi o {}'.format(maior))
print('O menor valor foi o {}'.format(menor))