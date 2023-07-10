# classes Biblioteca e Livro:
# A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# A biblioteca possui um metodo para alugar um livro. Caso o livro ja esteja alugado a pessoa nao podera alugar o livro.
# A biblioteca possui um metodo para devolver o livro.
# A biblioteca possui um metodo que devolve o nome do livro mais alugado.

class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1

    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis


class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)" % (nome, maior)
            return (ok, mensagem)

    def livrosOrdenadosPeloNome(self):
        # Ordenando Lista de Disponivies - BubbleSort
        elemento = self.disponiveis
        n = len(elemento) - 1
        troca = True
        while troca:
            troca = False
            for i in range(n):
                if elemento[i].nome > elemento[i + 1].nome:
                    elemento[i], elemento[i + 1] = elemento[i + 1], elemento[i]
                    troca = True
            n -= 1

        # Ordenando Lista de Alugados - BubbleSort
        elemento2 = self.alugados
        n = len(elemento2) - 1
        troca = True
        while troca:
            troca = False
            for i in range(n):
                if elemento2[i].nome > elemento2[i + 1].nome:
                    elemento2[i], elemento2[i + 1] = elemento2[i + 1], elemento2[i]
                    troca = True
            n -= 1

        # Merge - Ordena duas listas ja ordenadas
        i = j = 0
        resultado = []
        listaEsquerda = self.disponiveis
        listaDireita = self.alugados
        while i < len(listaEsquerda) and j < len(listaDireita):
            if listaEsquerda[i][1] <= listaDireita[j][1]:
                resultado.append(listaEsquerda[i])
                i += 1
            else:
                resultado.append(listaDireita[j])
                j += 1
        resultado += listaEsquerda[i:]
        resultado += listaDireita[j:]

        saida = []
        for i in range(len(resultado)):
            saida.append(resultado[i].codigo)
        return (saida)

# Entrada
lista = input().split(',')

# Inserindo livros automaticamente
b = Biblioteca()
qtd_livros = int(lista[0])
c = 1
for i in range(qtd_livros):
    l = Livro(int(lista[c]), lista[c + 1], lista[c + 2])
    b.inserir(l)
    c += 3

# Saida
print(*b.livrosOrdenadosPeloNome())
