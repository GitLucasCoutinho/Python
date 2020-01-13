# Programa para contar vogais em uma palavra

# Entrada
palavra = input("Digite uma palavra: ")

# Definindo as vogais
vogais = "aeiouAEIOU"

# Contador
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

# Saída
print(f"A palavra '{palavra}' possui {contador} vogais.")