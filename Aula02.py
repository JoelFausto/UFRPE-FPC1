# Aula 2 - Recursão

# Fibonacci - Modelo recursivo

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 0:
        return 'Não é possível calcular termos negativos!'
    else:
        return fib(n - 1) + fib(n - 2)


x = int(input('Qual termo de Fibonacci você deseja ver? '))
print(f'O {x}° termo de Fibonacci é: {fib(x)}')

# Fibonacci - Modelo interativo (loops)

k = int(input('Qual termo de Fibonacci você deseja ver? '))
if k == 1:
    print('O 1° termo é: 0')
elif k == 2:
    print('O 2° termo é: 1')
else:
    t1 = 0
    t2 = 1
    t3 = 0
    cont = 3
    while cont <= k:
        t3 = t2 + t1
        t1 = t2
        t2 = t3
        cont += 1
    print(f'O {k}° termo é: {t3}')
