# Função para inserção dos elementos na Tabela Hash
def insercao_hash(lista, elemento, qtd_containers, t_containers):
    conteiner = elemento % qtd_containers
    posicao = conteiner * t_containers
    for c in range(t_containers):
        if lista[posicao + c] is None:
            lista[posicao + c] = elemento
            break
    return lista

# Buscas de elementos e contagem de comparações
def busca_hash(lista, elemento, qtd_containers, t_containers):
    conteiner = elemento % qtd_containers
    posicao = conteiner * t_containers
    cont = 0
    for c in range(t_containers):
        cont += 1
        if lista[posicao + c] is None:
            break
        else:
            if lista[posicao + c] == elemento:
                break
    return cont

# Leitura
entrada = input().split()
for l in range(len(entrada)):
    entrada[l] = int(entrada[l])

qtde_containers = entrada[0]
tam_containers = entrada[1]
tam_ListaHash = qtde_containers * tam_containers
qtde_insercoes = entrada[2]

tabelaHash = [None] * tam_ListaHash

# Inserção de elementos que serão adicionados a tabela Hash
for i in range(3, qtde_insercoes + 3):
    tabelaHash = insercao_hash(tabelaHash, entrada[i], qtde_containers, tam_containers)

# Buscando elementos e retornando número de comparações
comp = []
for i in range((3 + qtde_insercoes), len(entrada)):
    comp.append(busca_hash(tabelaHash, entrada[i], qtde_containers, tam_containers))
print(*comp)
