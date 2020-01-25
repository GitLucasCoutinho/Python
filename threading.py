import threading
import time

# Função que imprime números de 1 a 50
def imprimir_numeros():
    for i in range(1, 51):
        print("Número:", i)
        time.sleep(0.05)  # pausa para simular concorrência

# Criando a thread
thread_numeros = threading.Thread(target=imprimir_numeros)

# Iniciando a thread
thread_numeros.start()

# Enquanto isso, a thread principal imprime letras
for letra in range(ord('A'), ord('Z') + 1):
    print("Letra:", chr(letra))
    time.sleep(0.1)  # pausa para simular concorrência

# Esperando a thread terminar antes de encerrar o programa
thread_numeros.join()