import random
import time

def gerador_aleatorio(inicial, final, numeros):
    random.seed(2026)

    numeros_aleatorios = []
    for i in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios

def insertion_sort_otimizado(numeros):
    start_time = time.time()

    for i in range(1, len(numeros)):
        valor = numeros[i]

        inicio = 0
        fim = i - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            if numeros[meio] > valor:
                fim = meio - 1
            else:
                inicio = meio + 1

        j = i
        while j > inicio:
            numeros[j] = numeros[j-1]
            j -= 1

        numeros[inicio] = valor

    end_time = time.time()
    return end_time - start_time

def main():
    lista_aleatoria = gerador_aleatorio(1, 20000, 10000)
    lista_ordenada = sorted(lista_aleatoria)
    lista_inversa = lista_ordenada[::-1]

    tempo_aleatoria = insertion_sort_otimizado(lista_aleatoria[:])
    print("Aleatória:", tempo_aleatoria)

    tempo_ordenada = insertion_sort_otimizado(lista_ordenada[:])
    print("Ordenada:", tempo_ordenada)

    tempo_inversa = insertion_sort_otimizado(lista_inversa[:])
    print("Inversa:", tempo_inversa)

main()