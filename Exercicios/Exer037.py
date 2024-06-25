'''
Exercício Python 037: Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
binário, 2 para octal e 3 para hexadecimal.
'''

n1=int(input('Digite um numero pra ser convertido'))
formato=int(input('Escolha uma das opções para ser convertidos: \n1 - Binario\n2 - Octal\n3 - Hexadecimal\n'))
if formato == 1:
    print('O numero {} convertido em Binario fica {}'.format(n1,bin(n1)[2:]))
elif formato == 2:
    print('O numero {} convertido em Octal fica {}'.format(n1,oct(n1)[2:]))
elif formato == 3:
    print('O numero {} convertido em Hexadecimal fica {}'.format(n1,hex(n1)[2:]))

