'''
Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
a = float(input('Digite o comprimento do primeiro segmento'))
b = float(input('Digite o comprimento do segundo segmento'))
c = float(input('Digite o comprimento do terceiro segmento'))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos formam um triangulo',end=' ')
    if a == b == c:
        print('Equilatero')
    elif a != b and a != c and b != c:
        print('Escaleno')
    elif a == b or a == c or b == c:
        print('Isósceles')
else:
    print('Os segmentos não formam um triangulo')