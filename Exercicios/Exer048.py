# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.
soma=0
for n in range(0, 501):
    if n % 3 ==0:
        soma = soma + n

print(str(n) + " " + str(soma))