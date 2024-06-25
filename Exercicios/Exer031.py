Km = float(input('Informe a distacia da Viagem desejada: '))

if Km<=200:
    valor = Km*0.50
    print('O valor da passagem de {}Km é R${:.2f}'.format(Km,valor))
else:
    valor = Km * 0.45
    print('O valor da passagem de {}Km é R${:.2f}'.format(Km,valor))
