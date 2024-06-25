a = float(input('Digite o comprimento do primeiro segmento'))
b = float(input('Digite o comprimento do segundo segmento'))
c = float(input('Digite o comprimento do terceiro segmento'))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos foram um triangulo')
else:
    print('Os segmentos não formam um triangulo')