entrada = input()

aberto = '([{'
fechado = ')]}'

def CasamentoPerfeito(string):
    pilha = []

    for elemento in string:
        if elemento in aberto:
            pilha.append(elemento)
        elif elemento in fechado:
            if len(pilha) > 0:
                if elemento == ')' and pilha[-1] == '(':
                    pilha.pop()
                elif elemento == ']' and pilha[-1] == '[':
                    pilha.pop()
                elif elemento == '}' and pilha[-1] == '{':
                    pilha.pop()
                else:
                    return 'casamento imperfeito'
            else:
                return 'casamento imperfeito'
    
    if len(pilha) == 0:
        return 'casamento perfeito'
    else:
        return 'casamento imperfeito'

print(CasamentoPerfeito(entrada))
