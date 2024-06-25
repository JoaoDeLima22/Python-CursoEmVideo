casa = int(input('Qual o valor da casa: '))
salario = int(input('Qual o valor do seu salario: '))
anos = int(input('Em quantos anos deseja pagar: '))

prestacao = casa /  (anos * 12)

if prestacao <= salario*0.3:
    print('A prestação ficou de R${:.2f} e o emprestimo foi aprovado'.format(prestacao))
elif prestacao >= (salario*0.3):
    print('A prestação ficou de R${:.2f} e o emprestimo foi negado'.format(prestacao))