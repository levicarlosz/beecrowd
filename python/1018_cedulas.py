# Descrição:
# Leia um valor inteiro N (0 < N < 1000000).
# Calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
# As notas disponíveis são: 100, 50, 20, 10, 5, 2 e 1 reais.

# Objetivo:
# Mostrar o valor lido e a quantidade mínima de cada tipo de nota necessária para compô-lo.

# Entrada:
# - Um valor inteiro N, onde 0 < N < 1000000.

# Saída:
# - O valor lido.
# - A quantidade de cada nota (de cima para baixo: 100 até 1), no seguinte formato:
#   X nota(s) de R$ Y,00
# - Cada linha deve terminar com uma quebra de linha (`\n`), ou será considerado erro de apresentação.

# Exemplo de Entrada e Saída:

# Entrada:
# 576

# Saída:
# 576
# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00

# Outro exemplo:

# Entrada:
# 11257

# Saída:
# 11257
# 112 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 0 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 1 nota(s) de R$ 2,00
# 0 nota(s) de R$ 1,00


cedulas = [100, 50, 20, 10, 5, 2, 1]
qtd_notas = []
N = int(input())

print(N)

for i in range(len(cedulas)):
    qtd = N // cedulas[i]
    N = N % cedulas[i]
    qtd_notas.append(qtd)
    print(f"{qtd_notas[i]} nota(s) de R$ {cedulas[i]},00")
    