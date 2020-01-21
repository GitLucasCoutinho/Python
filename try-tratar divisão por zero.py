# Programa para tratar divisão por zero

try:
    # Entrada de dados
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Operação de divisão
    resultado = num1 / num2
    print("Resultado da divisão:", resultado)

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")