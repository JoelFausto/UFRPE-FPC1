# Tabela Hash - Endereçamento aberto usando containers

# Funções para inserção de elementos nos containers da Tabela Hash
def insercao_hash(lista, elemento, qtd_containers, tam_containers):
    conteiner = elemento % qtd_containers
    posicao = conteiner * tam_containers
    for c in range(tam_containers):
        if lista[posicao + c] is None:
            lista[posicao + c] = elemento
            break
        elif c == tam_containers - 1:
            lista = insercao_overflow_hash(lista, elemento, qtd_containers, tam_containers)
    return lista


def insercao_overflow_hash(lista, elemento, qtd_containers, tam_containers):
    posicao = (qtd_containers * tam_containers)
    for c in range(posicao, len(lista)):
        if lista[c] is None:
            lista[c] = elemento
            break
    return lista

# Buscas de elementos e contagem de comparações
def busca_hash(lista, elemento, qtd_containers, tam_containers):
    conteiner = elemento % qtd_containers
    posicao = conteiner * tam_containers
    cont = 0
    for c in range(tam_containers):
        cont += 1
        if lista[posicao + c] is None:
            break
        else:
            if lista[posicao + c] == elemento:
                break
            elif c == tam_containers - 1:
                cont = busca_overflow_hash(lista, elemento, qtd_containers, tam_containers, cont)
    return cont


def busca_overflow_hash(lista, elemento, qtd_containers, tam_containers, cont):
    for c in range((qtd_containers * tam_containers), len(lista)):
        cont += 1
        if lista[c] is None:
            break
        else:
            if lista[c] == elemento:
                break
    return cont

# Entradas / Criação da Tabela Hash
entrada = list(map(int, input().split()))
qtd_containers = entrada[0]
tam_containers = entrada[1]
qtd_insercoes = entrada[3]
tabelaHash = [None] * ((qtd_containers * tam_containers) + entrada[2])

# Inserção de elementos que serão adicionados a tabela Hash
for i in range(4, qtd_insercoes + 4):
    tabelaHash = insercao_hash(tabelaHash, entrada[i], qtd_containers, tam_containers)
print(tabelaHash)

# Buscando elementos e retornando número de comparações
comp = []
for i in range((4 + qtd_insercoes), len(entrada)):
    comp.append(busca_hash(tabelaHash, entrada[i], qtd_containers, tam_containers))
print(*comp)
