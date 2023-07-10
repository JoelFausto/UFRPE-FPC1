x = float(input())
# Valores quando n é 0:
numerador = fatorial = fator = s = 1
for n in range(1, 50):
    # Cálculo Numerador
    numerador = numerador * (-1)
    # Cálculo Denominador
    fatorial = (n * 2) * ((n * 2) - 1) * fatorial
    denominador = fatorial
    # Cálculo X
    fator = fator * x * x
    # Cálculo Geral
    calc = (numerador / denominador) * fator
    # Somátorio
    s += calc
print("%.4f" % s)
