# Programa para criar um array de 10 números e calcular a média

# Array (lista) com 10 números
numeros = [5, 8, 12, 20, 7, 15, 3, 10, 18, 6]

# Cálculo da média
soma = sum(numeros)          # soma de todos os elementos
quantidade = len(numeros)    # quantidade de elementos
media = soma / quantidade    # média aritmética

# Saída
print("Números:", numeros)
print("Soma:", soma)
print("Quantidade:", quantidade)
print("Média:", media)