# Descrição:
# Leia quatro valores inteiros: A, B, C e D.
# Em seguida, calcule e mostre a diferença entre o produto de A e B
# e o produto de C e D, segundo a seguinte fórmula:
# DIFERENCA = (A * B - C * D)

# Entrada:
# O programa deve ler 4 valores inteiros, um por linha.

# Saída:
# Imprima a mensagem "DIFERENCA", em letras maiúsculas, seguida de um espaço,
# um sinal de igual com espaços antes e depois, e o valor calculado.
# Finalize a saída com uma quebra de linha para evitar "Presentation Error".

# Fórmula:
# DIFERENCA = (A × B) - (C × D)

# Exemplos de Entrada e Saída:
# +------------------+--------------------+
# | Entrada          | Saída              |
# +------------------+--------------------+
# | 5 6 7 8          | DIFERENCA = -26    |
# | 0 0 7 8          | DIFERENCA = -56    |
# | 5 6 -7 8         | DIFERENCA = 86     |
# +------------------+--------------------+

A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = A * B - C * D

print(f"DIFERENCA = {DIFERENCA}")
