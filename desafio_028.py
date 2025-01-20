# --- DESAFIO 028 ---
#Crie um programa que faça o computador gerar um numero aleatorio de 0 a 5 e  peça ao user para adivinhar o numero.O programa retornará se o user venceu ou perdeu

from random import randrange
print("### JOGO DA ADIVINHAÇAO ###")

print("Computador esta pensando em um numero de 0 a 5...")
number = randrange(0, 6)
input = int(input("Adivinhe o numero: "))

print("PARABENSS VOCE ACERTOU" if input == number else "Voce errou, otario, o numero correto era {}".format(number))


