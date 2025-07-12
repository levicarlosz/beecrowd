# Descrição:
# Leia um valor inteiro que representa o tempo de duração de um evento em segundos.
# O objetivo é converter esse tempo para o formato: horas:minutos:segundos.

# Entrada:
# - Um valor inteiro N, representando o tempo total do evento em segundos.

# Saída:
# - O tempo convertido para o formato: H:M:S
#   Onde H = horas, M = minutos, S = segundos.
#   Todos os valores devem ser inteiros e separados por dois-pontos ":".

# Exemplos de Entrada e Saída:
# +------------+------------+
# |  Entrada   |   Saída    |
# +------------+------------+
# |   556      |   0:9:16   |
# |     1      |   0:0:1    |
# | 140153     |  38:55:53  |
# +------------+------------+



N = int(input())

horas = N // 3600
minutos = (N % 3600) // 60
segundos = N % 60


print(f'{horas}:{int(minutos)}:{int(segundos)}')