salario = float(input('Digite o valor do seu salario: '))
if salario<=1250:
    aumento = (salario *1.15)
    print('Seu salario era de R${:.2f} e foi para {:.2f}'.format(salario, aumento))
else:
    aumento = (salario * 1.1)
    print('Seu salario era de R${:.2f} e foi para {:.2f}'.format(salario,aumento))