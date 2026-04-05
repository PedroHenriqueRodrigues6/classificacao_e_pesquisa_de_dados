import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def selection_sort_nao_otimizado(arr):
    start_time = time.time()
    n=len(arr)

    for j in range(n-1):
        maior=j

        for i in range(j+1,n):
            if arr[i]>arr[maior]:
                maior=i

        arr[j], arr[maior]= arr[maior], arr[j]

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = selection_sort_nao_otimizado(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = selection_sort_nao_otimizado(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = selection_sort_nao_otimizado(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()