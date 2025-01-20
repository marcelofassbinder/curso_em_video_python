# --- DESAFIO 053  ---
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().replace(" ", "")
len = len(frase)
for c in range(0, len):
    if (frase[c] != frase[len - 1]):
        print('NÃO É UM PALINDROMO :(')
        exit(0)
    len -= 1
print('É UM PALINDROMO :)')
