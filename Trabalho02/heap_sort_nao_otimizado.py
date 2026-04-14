import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def max_heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        max_heapify(arr, n, maior)

def heap_sort_nao_otimizado(arr):
    start_time = time.time()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        max_heapify(arr, j, 0)

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = heap_sort_nao_otimizado(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = heap_sort_nao_otimizado(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = heap_sort_nao_otimizado(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()