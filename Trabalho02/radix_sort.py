import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def counting_sort_numeros(arr, pos):
    n = len(arr)
    saida = [0] * n
    count = [0] * 10

    for i in range(n):
        digit = (arr[i] // pos) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // pos) % 10
        saida[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = saida[i]

def radix_sort_numeros(arr):
    start_time = time.time()

    max_num = max(arr)

    pos = 1
    while max_num // pos > 0:
        counting_sort_numeros(arr, pos)
        pos *= 10

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = radix_sort_numeros(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = radix_sort_numeros(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = radix_sort_numeros(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()