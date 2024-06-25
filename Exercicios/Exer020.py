import random

aluno1 = str(input('Digite o nome do primeiro aluno(a)'))
aluno2 = str(input('Digite o nome do segundo aluno(a)'))
aluno3 = str(input('Digite o nome do terceiro aluno(a)'))
aluno4 = str(input('Digite o nome do quarto aluno(a)'))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('a ordem da apresentação será : {}'.format(lista))
