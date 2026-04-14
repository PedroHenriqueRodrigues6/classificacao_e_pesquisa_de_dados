import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def counting_sort(arr):
    start_time = time.time()

    max_val = max(arr)
    n = len(arr)

    count = [0] * (max_val + 1)

    saida = [0] * n

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        saida[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = counting_sort(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = counting_sort(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = counting_sort(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()