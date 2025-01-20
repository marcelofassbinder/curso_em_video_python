# --- DESAFIO 025 ---

#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Digite seu nome: ")).title()

print("O nome inserido possui Silva? {}".format('Silva' in nome))