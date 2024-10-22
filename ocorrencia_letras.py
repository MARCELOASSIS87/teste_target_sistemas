# Solicita ao usuário uma string
texto = input("Digite uma string: ")
if texto == '':
    print("Você não digitou nada.")

# Inicializa o contador de ocorrências da letra 'a'
contador = 0

# Percorre cada caractere na string
for caractere in texto:
    # Verifica se o caractere é 'a' ou 'A'
    if caractere == 'a' or caractere == 'A':
        contador += 1

# Verifica se a letra 'a' foi encontrada e exibe o resultado
if contador > 0:
    print(f"A letra 'a' aparece {contador} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
