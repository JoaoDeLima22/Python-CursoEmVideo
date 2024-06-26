'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''

peso=float(input('Qual o seu peso: '))
altura=float(input('Qual a sua altura: '))
imc=peso/(altura**2)

if imc<=18.5:
    print('Seu IMC é {:.2f} e esta Abaixo do peso'.format(imc))
elif imc<=25:
    print('Seu IMC é {:.2f} e esta Peso ideal'.format(imc))
elif imc<=30:
    print('Seu IMC é {:.2f} e esta Sobrepeso'.format(imc))
elif imc<=40:
    print('Seu IMC é {:.2f} e esta Obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f} e esta Obesidade Morbida'.format(imc))