# --- DESAFIO 051    ---
#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressao Aritmetica. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 1
for c in range(termo, (razao * 10) + termo, razao):
    print('{}º ->'.format(cont), end=" ")
    print(c)
    cont+=1
