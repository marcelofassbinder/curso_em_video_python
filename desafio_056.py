# --- DESAFIO 056  ---
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
idade_homem_velho = 0
nome_velho = ''
mulheres_mais_de_vinte = 0
for c in range(0, 4):
    nome = (str(input(f'Nome da {c + 1}ª pessoa: ')))
    idade = (int(input(f'Idade da {c + 1}ª pessoa: ')))
    sexo = (str(input(f'Sexo da {c + 1}ª pessoa[M/F]: ')).upper().strip())
    soma_idades += idade
    if c == 1 and sexo == "M":
        idade_homem_velho = idade
        nome_velho = nome
    elif sexo == "M" and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_mais_de_vinte += 1
media = soma_idades / 4
print(f'A média de idade do grupo é de {media} anos')
if nome_velho == "":
    print('Nao ha homens no grupo')
else:
    print(f'O homem mais velho tem {idade_homem_velho} e se chama {nome_velho.title()}')
print(f'Ha {mulheres_mais_de_vinte} mulheres com menos de 20 anos')