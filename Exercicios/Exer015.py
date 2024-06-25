dias = int(input('O carro foi alugado por quantos dias?'))
km = float(input('Quantos Km foram rodados'))
aluguel = (dias * 60) + (0.15 * km)

print('Então o carro foi alugado por {} dias e teve {}km rodados nesse tempo, o total a pagar foi de {}'.format(dias, km, aluguel))
