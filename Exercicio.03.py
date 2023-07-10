from math import floor

def busca_binaria(lista, item, inicio=0, fim=None, cont=1):
    # Casos Base
    if fim is None:
        fim = len(lista) - 1
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return 1
    # Passo Recursivo
    else:
        if inicio <= fim:
            if (inicio + fim) % 2 != 0:
                media = floor((inicio + fim) / 2) + 1
            else:
                media = floor((inicio + fim) / 2)
            if lista[media] == item:
                return cont
            if item < lista[media]:
                cont += 1
                return busca_binaria(lista, item, inicio, media - 1, cont)
            else:
                cont += 1
                return busca_binaria(lista, item, media + 1, fim, cont)
    # Caso item não seja encontrado
    return cont - 1


listaCompleta = input().split()
for l in range(len(listaCompleta)):
    listaCompleta[l] = int(listaCompleta[l])

# Verificação se a entrada foi vazia
if len(listaCompleta) != 0:
    numeroBuscado = listaCompleta[0]
    listaNova = listaCompleta[1:]
else:
    numeroBuscado = 0
    listaNova = []

print(busca_binaria(listaNova, numeroBuscado))