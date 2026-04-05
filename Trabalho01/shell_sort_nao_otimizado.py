import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def shell_sort_nao_otimizado(arr):
    start_time = time.time()
    n=len(arr)
    h=n//2
    while h>0:
        for i in range(h, n):
            k=i
            valor=arr[i]
            while k>=h and valor<arr[k-h]:
                arr[k]=arr[k-h]
                k-=h
            arr[k]=valor
        h//=2

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = shell_sort_nao_otimizado(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = shell_sort_nao_otimizado(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = shell_sort_nao_otimizado(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()