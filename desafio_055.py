# --- DESAFIO 055  ---
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista =[]
for c in range(0, 5):
    lista.append(float(input('Digite o peso da {}ª pessoa: '.format(c + 1))))
print('O menor peso é de {} kg'. format(min(lista)))
print('O maior peso é de {} kg'.format(max(lista)))