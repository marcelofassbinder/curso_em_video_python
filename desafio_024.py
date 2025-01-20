# --- DESAFIO 024 ---

#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com "SANTO"

city = str(input("Digite o nome de uma cidade: ")).strip()

print("A cidade {} começa com SANTO?")
print('Santo' in city[:5].title())
