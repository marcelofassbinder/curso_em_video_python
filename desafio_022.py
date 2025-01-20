# --- DESAFIO 022 ---

#Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 -O nome com todas as letras maiusculas.
# 2- O nome com todas as letras minusculas.
# 3 - Quantas letras tem? sem considerar espaços
# 4 - Quantas letras tem o primeiro nome?

nome = input(str('Digite seu nome completo->  '))

print('Nome com letras maiusculas = {}'.format(nome.upper()))
print('Nome com letras minusculas = {}'.format(nome.lower()))
print('Quantas letras tem? sem espaços = {}'.format(len(nome) - nome.count(' ')))
print('Quantas letras tem o primeiro nome? = {}'.format(len(nome.split()[0])))
