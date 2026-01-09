# Função que retorna o maior entre dois números
def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

# Testando a função
num1 = 15
num2 = 27

resultado = maior_numero(num1, num2)
print("O maior número é:", resultado)