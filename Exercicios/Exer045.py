'''
Crie um programa que faça o computador jogar Jokenpô com você.
lista = ["pedra", "papel", "tesoura"]
'''
'''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
'''
from random import randint
from time import sleep

print('Selecione uma opção: \n1 - pedra\n2 - papel\n3 - tesoura')
opcao = int(input("Qual sua opcao? "))
maquina = randint(1, 3)
if opcao == 1:
    n1 = 'pedra'
elif opcao == 2:
    n1 = 'papel'
elif opcao == 3:
    n1 = 'tesoura'
else:
    print('selecione uma opção valida')
    exit()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")
if maquina == 1:
    n2 = 'pedra'
elif maquina == 2:
    n2 = 'papel'
elif maquina == 3:
    n2 = 'tesoura'
print('Você escolheu {}  \n A maquina escolheu {}'.format(n1, n2))
if n1 == n2:
    print('Empate')
elif n1 =='pedra' and n2=='papel' or n1 =='papel' and n2=='tesoura' or n1 =='tesoura' and n2=='pedra' :
     print('Computador ganhou')
else:
    print('Você ganhou')