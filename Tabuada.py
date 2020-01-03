# Programa para gerar a tabuada de um número escolhido pelo usuário

# Entrada
numero = int(input("Digite um número para ver sua tabuada: "))

# Laço for para gerar a tabuada de 1 a 10
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")