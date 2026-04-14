import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def quick_sort_nao_otimizado(arr):
    if len(arr) <= 1:
        return arr

    pivo = arr[len(arr)//2]
    menores = []
    maiores = []
    iguais = []

    for i in arr:
        if i < pivo:
            menores.append(i)
        elif i > pivo:
            maiores.append(i)
        else:
            iguais.append(i)

    return quick_sort_nao_otimizado(menores) + iguais + quick_sort_nao_otimizado(maiores)

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    start = time.time()
    quick_sort_nao_otimizado(lista_aleatoria[:])
    print("Aleatória:", time.time() - start)

    start = time.time()
    quick_sort_nao_otimizado(lista_ordenada[:])
    print("Ordenada:", time.time() - start)

    start = time.time()
    quick_sort_nao_otimizado(lista_inversa[:])
    print("Inversa:", time.time() - start)

main()