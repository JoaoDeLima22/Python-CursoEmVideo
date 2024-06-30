''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''
tabuada = int(input("Informe um numero:"))
for n in range(1, 11):
    print(str(n) + " x " + str(tabuada) + " = " + str(n * tabuada) )