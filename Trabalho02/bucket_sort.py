import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    start_time = time.time()

    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr

    n = len(arr)

    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n + 1)]

    for num in arr:
        if num == max_val:
            index = n - 1
        else:
            index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    for i in range(n):
        insertion_sort(buckets[i])

    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = bucket_sort(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = bucket_sort(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = bucket_sort(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()