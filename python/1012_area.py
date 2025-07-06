# Descrição:
# Escreva um programa que leia três valores de ponto flutuante de dupla precisão: A, B e C.
# Em seguida, calcule e mostre as seguintes áreas:

# a) A área do triângulo retângulo que tem A por base e C por altura.
# b) A área do círculo de raio C. (Use π = 3.14159)
# c) A área do trapézio que tem A e B por bases e C por altura.
# d) A área do quadrado que tem lado B.
# e) A área do retângulo que tem lados A e B.

# Entrada:
# O programa deve ler 3 valores de ponto flutuante com um dígito após o ponto: A, B e C.

# Saída:
# O programa deve imprimir 5 linhas, cada uma com a mensagem correspondente e o valor da área,
# com exatamente 3 casas decimais.
# Formato da saída:
# - Deve haver um espaço entre os dois pontos ":" e o valor.
# - Finalize cada linha com uma quebra de linha para evitar "Presentation Error".


# Exemplos de Entrada e Saída:
# +-------------------------+------------------------------+
# | Entrada                | Saída                         |
# +-------------------------+------------------------------+
# | 3.0 4.0 5.2            | TRIANGULO: 7.800              |
# |                        | CIRCULO: 84.949               |
# |                        | TRAPEZIO: 18.200              |
# |                        | QUADRADO: 16.000              |
# |                        | RETANGULO: 12.000             |
# |------------------------|------------------------------|
# | 12.7 10.4 15.2         | TRIANGULO: 96.520             |
# |                        | CIRCULO: 725.833              |
# |                        | TRAPEZIO: 175.560             |
# |                        | QUADRADO: 108.160             |
# |                        | RETANGULO: 132.080            |
# +------------------------+------------------------------+


ENTRADAS = input().split()

A = float(ENTRADAS[0])
B = float(ENTRADAS[1])
C = float(ENTRADAS[2])

PI = 3.14159

TRIANGULO = (A * C) / 2
CIRCULO = PI * (C**2)
TRAPEZIO = ((A+B) * C) / 2
QUADRADO = B ** 2
RETANGULO = A * B

print(f"TRIANGULO: {TRIANGULO:.3f}")
print(f"CIRCULO: {CIRCULO:.3f}")
print(f"TRAPEZIO: {TRAPEZIO:.3f}")
print(f"QUADRADO: {QUADRADO:.3f}")
print(f"RETANGULO: {RETANGULO:.3f}")
