import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def insertion_sort(vetor, inicio, fim):
    for i in range(inicio + 1, fim + 1):
        chave = vetor[i]
        j = i - 1
        while j >= inicio and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

def merge(vetor, inicio, meio, fim, auxiliar):
    if meio < fim and vetor[meio] <= vetor[meio + 1]:
        return

    for i in range(inicio, fim + 1):
        auxiliar[i] = vetor[i]

    i = inicio
    j = meio + 1
    k = inicio

    while i <= meio and j <= fim:
        if auxiliar[i] <= auxiliar[j]:
            vetor[k] = auxiliar[i]
            i += 1
        else:
            vetor[k] = auxiliar[j]
            j += 1
        k += 1

    while i <= meio:
        vetor[k] = auxiliar[i]
        i += 1
        k += 1

def merge_sort_otimizado(vetor, LIMIAR=32):
    n = len(vetor)
    auxiliar = [0] * n

    for inicio in range(0, n, LIMIAR):
        fim = min(inicio + LIMIAR - 1, n - 1)
        insertion_sort(vetor, inicio, fim)

    tamanho = LIMIAR
    while tamanho < n:
        for inicio in range(0, n, tamanho * 2):
            meio = min(inicio + tamanho - 1, n - 1)
            fim = min(inicio + 2 * tamanho - 1, n - 1)

            if meio < fim:
                merge(vetor, inicio, meio, fim, auxiliar)

        tamanho *= 2

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    start = time.time()
    merge_sort_otimizado(lista_aleatoria[:])
    end = time.time()
    print("Aleatória:", end - start)

    start = time.time()
    merge_sort_otimizado(lista_ordenada[:])
    end = time.time()
    print("Ordenada:", end - start)

    start = time.time()
    merge_sort_otimizado(lista_inversa[:])
    end = time.time()
    print("Inversa:", end - start)

main()