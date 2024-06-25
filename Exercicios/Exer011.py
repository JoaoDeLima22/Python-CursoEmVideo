l= float(input('informe o valor da largura da parede em metros:'))
h = float(input('informe o valor da altura da parede em metros:'))
area = l*h
Quant = area/2
print('O valor informado foi {:.2f}m de altura e {:.2f}m de largura e a area será de {:.2f}m² e será necessario {:.2f}l de tinta'.format(h, l, area, Quant))