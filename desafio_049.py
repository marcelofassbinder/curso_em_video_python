# --- DESAFIO 049    ---
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input('Digite um numero inteiro: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(number, c, number * c))