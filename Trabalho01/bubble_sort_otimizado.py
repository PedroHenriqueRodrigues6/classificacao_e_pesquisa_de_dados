import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def bubble_sort_otimizado(arr):
    start_time = time.time()
    n=len(arr)-1

    for i in range(n-1):
        k=0
        while k<n-i:
            if arr[k]>arr[k+1]:
                arr[k], arr[k+1]= arr[k+1], arr[k]
            k+=1

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = bubble_sort_otimizado(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = bubble_sort_otimizado(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = bubble_sort_otimizado(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()