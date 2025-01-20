# --- DESAFIO 026 ---

#Crie um programa que leia uma frase e mostre:
# 1- Quantas vezes aparce a letra 'a'
# 2 - Em que posicao ela aparece a primeira vez
# 3 - Em que posicao ela aparece a ultima vez.

frase = str(input("Digite uma frase: ")).lower()

print("A letra 'a' aparece {} vezes".format(frase.count('a')))

if (frase.count('a') > 0):
    print("A posicao em que 'a' aparece pela primeira vez eh: {}".format(frase.find('a')))
    print("A posicao em que 'a' aparece pela última vez é: {}".format(frase.rfind('a')))
