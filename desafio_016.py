# --- DESAFIO 016 --- #

#Crie um programa que leia um numero real qualquer e mostre na tela sua porçao inteira

from math import floor
a = float(input('Digite um numero: '))
b = floor(a)
print('A parte inteira de {} é {}'.format(a, b))