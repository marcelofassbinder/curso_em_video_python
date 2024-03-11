# --- DESAFIO 020 ---

#Agora o professor quer sortear a ordem de apresentaçao de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)

print('A ordem sorteada é a seguinte.\n1) {}\n2) {}\n3) {}\n4) {}'.format(lista[0], lista[1], lista[2], lista[3]))