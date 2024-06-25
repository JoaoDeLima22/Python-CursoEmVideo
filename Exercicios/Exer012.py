valor = float(input('Qual o preço do produto? R$'))
valorf = valor-(valor*0.05)
print('o valor do produto é R${:.2f} e na promoção o valor vai para R${:.2f}'.format(valor, valorf))