# Lista, Filas e Pilhas

expressao = input()

# Metódo 1
'''filaP = []
pilhaP = []
filaC = []
pilhaC = []
filaT = []
pilhaT = []
for s in expressao:
    if s == '(':
        filaP.append(s)
    if s == ')':
        pilhaP.append(s)
    if s == '{':
        filaC.append(s)
    if s == '}':
        pilhaC.append(s)
    if s == '[':
        filaT.append(s)
    if s == ']':
        pilhaT.append(s)
if len(filaP) == len(pilhaP) and len(filaC) == len(pilhaC) and len(filaT) == len(pilhaT):
    print('casamento perfeito')
else:
    print('casamento imperfeito')'''

# Metódo 2
def validacao_exp(string):
    pilha = []
    resultado = None
    for l in range(len(string) - 1):
        if string[l] in '([{':
            pilha.append(string[l])
        else:
            if string[l] in ')]}':
                if not pilha:
                    resultado = 'casamento imperfeito'
                    return resultado
                else:
                    if string[l] == ')' and pilha[-1] == '(':
                        pilha.pop()
                    elif string[l] == ']' and pilha[-1] == '[':
                        pilha.pop()
                    elif string[l] == '}' and pilha[-1] == '{':
                        pilha.pop()
                    else:
                        resultado = 'casamento imperfeito'
                        return resultado
    if resultado is None:
        return 'casamento perfeito'

print(validacao_exp(expressao))
