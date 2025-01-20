# --- DESAFIO 045 ---
#Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep
print('---- JOKENPO GAME ----')
print('Suas opcoes sao:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogada = int(input('Digite sua jogada: '))
if jogada < 0 or jogada > 2:
    print('JOGADA INVALIDA')
    exit(0)
computador = random.randrange(-1, 3, 1)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
print('- =' * 10)
print('Voce jogou {}'.format(opcoes[jogada]))
print('Computador jogou {}'.format(opcoes[computador]))
print('- =' * 10)

if jogada == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('COMPUTADOR VENCE')
    elif computador == 2:
        print('JOGADOR VENCE')
elif jogada == 1:
    if computador == 0:
        print('JOGADOR VENCE')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR VENCE')
elif jogada == 2:
    if computador == 0:
        print('COMPUTADOR VENCE')
    elif computador == 1:
        print('JOGADOR VENCE')
    elif computador == 2:
        print('EMPATE')
