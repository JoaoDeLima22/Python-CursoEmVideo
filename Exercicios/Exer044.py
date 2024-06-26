'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''

valor = float(input('Digite o valor do produto: '))
print('Selecione uma forma de pagamento:\n1 - à vista dinheiro/cheque \n2 - à vista no cartão\n3 - até 2x no cartão\n4 - em 3 ou mais vezes no cartão')
opcao= int(input('Escolha a opcao de pagamento: '))

if opcao == 1:
    valorf= valor - (valor*0.1)
    print('O valor do produto era de R${} e saiu por R${}'.format(valor,valorf))
elif opcao == 2:
    valorf= valor - (valor*0.05)
    print('O valor do produto era de R${} e saiu por R${}'.format(valor, valorf))
elif opcao == 3:
    print('O valor do produto saiu por {} não possui desconto'.format(valor))
elif opcao == 4:
    valorf= valor + (valor*0.2)
    print('O valor do produto era de R${} e saiu por R${}'.format(valor,valorf))
else:
    print('selecione uma opcao valida')