# --- DESAFIO 052    ---
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number= int(input('Digite um numero inteiro: '))
for c in range(number - 1, 1, -1):
    if (number % c == 0):
        print('NÃO É PRIMO')
        exit(0)
print("É PRIMO!!!!!")