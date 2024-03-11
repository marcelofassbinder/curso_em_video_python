# --- DESAFIO 018 ---

#Crie um programa que leia um angulo qualquer e mostre o valor do seno, cosseno e tangente.

import math
a = float(input('Digite um angulo: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O angulo {}º tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(a, sen, cos, tan))
