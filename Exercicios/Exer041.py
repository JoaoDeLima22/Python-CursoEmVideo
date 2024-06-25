'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 25 anos: sênior
acima de 20: master
'''


from datetime import date

ano = date.today().year
n1 = int(input('Informe o ano do seu nascimento: '))
idade = ano - n1

if idade <=9:
  print('Você tem {} ano e é Categoria Mirim'.format(idade))
elif idade <= 14:
  print('Você tem {} ano e é Categoria infantil'.format(idade))
elif idade <= 19:
  print('Você tem {} ano e é Categoria júnior'.format(idade))
elif idade <= 25:
  print('Você tem {} ano e é Categoria sênior'.format(idade))
else:
  print('Você tem {} ano e é Categoria Master'.format(idade))