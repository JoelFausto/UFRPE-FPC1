# Métodos de Organização
vetor = [2, 8, 1, 56, 37, 22, 71, 82, 90, 0, 4, 78, 15]


def bubbleSort(lista):
    troca = True
    n = len(lista) - 1
    while troca:
        troca = False
        for i in range(n):
            if lista[i] > lista[i + 1]:
                chave = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = chave
                troca = True
        n -= 1
    return lista


def insertionSort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i
        while j > 0 and lista[j - 1] > chave:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = chave
    return lista


def shellSort(lista):
    n = len(lista)
    h = int(n / 2)
    while h > 0:
        for i in range(h, n):
            chave = lista[i]
            j = i
            while j >= h and chave < lista[j - h]:
                lista[j] = lista[j - h]
                j = j - h
            lista[j] = chave
        h = int(h / 2.2)
    return lista


def selectionSort(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


def merge(lista, aux, esquerda, meio, direita):
    # Combina dois vetores ordenados em um único vetor (também ordenado).

    for k in range(esquerda, direita + 1):
        aux[k] = lista[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            lista[k] = aux[j]
            j += 1
        elif j > direita:
            lista[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            lista[k] = aux[j]
            j += 1
        else:
            lista[k] = aux[i]
            i += 1
    return lista

def mergesort(lista, aux, esquerda, direita):
    if direita <= esquerda:
        return lista
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort(lista, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort(lista, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge(lista, aux, esquerda, meio, direita)
    return lista

auxiliar = [0] * len(vetor)

def quickSort(lista):
    if len(lista) <= 1:
        return lista
    menor, igual, maior = [], [], []
    pivor = lista[0]
    for i in lista:
        if i < pivor:
            menor.append(i)
        elif i == pivor:
            igual.append(i)
        else:
            maior.append(i)
    return quickSort(menor) + igual + quickSort(maior)

print(bubbleSort(vetor), insertionSort(vetor), shellSort(vetor))
print(selectionSort(vetor), mergesort(vetor, auxiliar, 0, len(vetor) - 1), quickSort(vetor))
