# Função que retorna a Palavra Fibonacci
def palavrafib(n):
    if n == 0:
        return 'b'
    elif n == 1:
        return 'a'
    elif n > 1:
        return palavrafib(n - 1) + palavrafib(n - 2)


# Entrada
x = int(input())

# Saída
print(palavrafib(x))
