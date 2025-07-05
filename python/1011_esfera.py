# Descrição:
# Faça um programa que calcule e mostre o volume de uma esfera, dado o valor do seu raio (R).
# A fórmula para calcular o volume da esfera é:
# VOLUME = (4/3.0) * π * R³

# Observação:
# A constante π (pi) deve ser considerada como 3.14159.
# Use (4/3.0) ou (4.0/3) para evitar problemas com divisão inteira em algumas linguagens.

# Entrada:
# O programa deve ler um número de ponto flutuante (double), que representa o raio da esfera.

# Saída:
# O programa deve imprimir:
# - A mensagem "VOLUME = X", onde X é o volume calculado com 3 casas decimais.
# - Deve haver um espaço antes e depois do sinal de igual "=".
# - Finalize a saída com uma quebra de linha para evitar "Presentation Error".

# Fórmula:
# VOLUME = (4.0 / 3) * π * R³
# π = 3.14159

# Exemplos de Entrada e Saída:
# +----------+----------------------------+
# | Entrada  | Saída                      |
# +----------+----------------------------+
# | 3        | VOLUME = 113.097           |
# |----------|----------------------------|
# | 15       | VOLUME = 14137.155         |
# |----------|----------------------------|
# | 1523     | VOLUME = 14797486501.627   |
# +----------+----------------------------+

RAIO = float(input())
PI = 3.14159
VOLUME = (4 / 3.0) * PI * RAIO**3
print(f'VOLUME = {VOLUME:.3f}')
