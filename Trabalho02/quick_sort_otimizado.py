import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def quick_sort_otimizado(arr):
    if len(arr) <= 1:
        return arr

    pivo = random.choice(arr)

    menores = []
    iguais = []
    maiores = []

    for x in arr:
        if x < pivo:
            menores.append(x)
        elif x == pivo:
            iguais.append(x)
        else:
            maiores.append(x)

    return quick_sort_otimizado(menores) + iguais + quick_sort_otimizado(maiores)

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    start = time.time()
    quick_sort_otimizado(lista_aleatoria[:])
    print("Aleatória:", time.time() - start)

    start = time.time()
    quick_sort_otimizado(lista_ordenada[:])
    print("Ordenada:", time.time() - start)

    start = time.time()
    quick_sort_otimizado(lista_inversa[:])
    print("Inversa:", time.time() - start)

main()