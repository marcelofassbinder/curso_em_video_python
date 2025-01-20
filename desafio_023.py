# --- DESAFIO 023 ---

#Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados:
# Ex: numero = 1864
# unidade -> 4.
# dezena -> 6.
# centena -> 8.
# milhar -> 1.

number = '-1'
while(int(number) < 0 or int(number) > 9999):
    number = str(input("Digite um numero de 0 a 9999: ")).strip()
print('unidade-> {}' .format(number[len(number) - 1]))
if (len(number) >= 2):
    print('dezena-> {}' .format(number[len(number) - 2]))
if (len(number) >= 3):
    print('centena-> {}' .format(number[len(number) - 3]))
if (len(number) >= 4):
    print('milhar-> {}' .format(number[len(number) - 4]))

print("FAZENDO COMO INTEGER")
number = -1
while(number < 0 or number > 9999):
    number = int(input("Digite um numero de 0 a 9999: "))
print('unidade-> {}' .format(number % 10))
print('dezena-> {}' .format(number//10 % 10))
print('centena-> {}' .format(number//100 % 10))
print('milhar-> {}' .format(number//1000 % 10))
