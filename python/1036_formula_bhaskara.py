# Descrição:
# Leia três valores de ponto flutuante (A, B e C) e efetue o cálculo das raízes da equação de Bhaskara.
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
# caso haja uma divisão por 0 ou raiz de número negativo.

# Entrada:
# - Três valores de ponto flutuante (double): A, B e C

# Saída:
# - Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
# - Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
#   com uma mensagem correspondente conforme o exemplo abaixo.
# - Imprima sempre o final de linha após cada mensagem.

# Exemplos de Entrada e Saída:
# +-----------------------+-----------------------------+
# | Entrada               | Saída                       |
# +-----------------------+-----------------------------+
# | 10.0 20.1 5.1         | R1 = -0.29788               |
# |                       | R2 = -1.71212               |
# |-----------------------|-----------------------------|
# | 0.0 20.0 5.0          | Impossivel calcular         |
# |-----------------------|-----------------------------|
# | 10.3 203.0 5.0        | R1 = -0.02466               |
# |                       | R2 = -19.68408              |
# |-----------------------|-----------------------------|
# | 10.0 3.0 5.0          | Impossivel calcular         |
# +-----------------------+-----------------------------+


A, B, C = map(float, input().split())

delta = B**2 - ((A * C) * 4)


if delta >= 0 and A != 0:
    R1 = ((B * -1) + (delta**0.5)) / (2 * A)
    R2 = ((B * -1) - (delta**0.5)) / (2 * A)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")

