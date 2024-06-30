''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''
prim = int(input("Primeiro termo: \n"))
pa = int(input("Digite a razão da PA: \n"))
n = prim + (10 - 1) * pa
for c in range(prim, n, pa):
    print("{}".format(c), end=",")
print("\nFim.")
