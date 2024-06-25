velocidade = float(input('qual a velocidade do veiculo ?'))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('sua multa é de R${:.2f}' .format(multa))
else:
    print('Muito bem você não recebeu uma multa, dirija com cuidado')