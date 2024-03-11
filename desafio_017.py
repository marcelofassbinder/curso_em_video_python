# --- DESAFIO 017 --- #

#Crie um programa que leia o cateto adjascente e o cateto oposto de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math
adj = float(input('Digite o valor do cateto adjascente: '))
opo = float(input('Digite o valor do cateto oposto: '))

hip = math.sqrt(math.pow(adj, 2) + math.pow(opo, 2))

print('A hipotenusa deste triangulo vale {:.2f}'.format(hip))