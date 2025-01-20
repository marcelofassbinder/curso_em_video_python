# --- DESAFIO 027 ---

#Crie um programa que leia o nome completo de uma pessoa e mostre o seu primeiro e ultimo nome:

nome = str(input(("Digite seu nome completo: "))).strip().title()
split = nome.split()

print("Primeiro nome: {}".format(split[0]))
print("Ultimo nome: {}".format(split[len(split) - 1]))
