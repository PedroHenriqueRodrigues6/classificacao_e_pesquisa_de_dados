import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def merge_sort_nao_otimizado(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    esquerda = arr[:mid]
    direita = arr[mid:]

    esquerda = merge_sort_nao_otimizado(esquerda)
    direita = merge_sort_nao_otimizado(direita)

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    start = time.time()
    merge_sort_nao_otimizado(lista_aleatoria[:])
    end = time.time()
    print("Aleatória:", end - start)

    start = time.time()
    merge_sort_nao_otimizado(lista_ordenada[:])
    end = time.time()
    print("Ordenada:", end - start)

    start = time.time()
    merge_sort_nao_otimizado(lista_inversa[:])
    end = time.time()
    print("Inversa:", end - start)

main()
