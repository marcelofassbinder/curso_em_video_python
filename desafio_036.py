# --- DESAFIO 036 ---
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salario: R$'))
anos = int(input('Em quanto anos quer pagar? '))
meses = anos * 12
prestacao = casa / meses

print('Para pagar uma casa de R${:.2f} em {} anos, a prestacao sera de R${:.2f}'.format(casa, anos, prestacao))
if prestacao > (salario * 0.3):
    print('EMPRESTIMO NEGADO!')
else:
    print('EMPRESTIMO APROVADO!')
