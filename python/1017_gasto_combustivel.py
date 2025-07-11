# Descrição:
# Joaozinho quer calcular a quantidade de litros de combustível gastos em uma viagem.
# O automóvel utilizado faz 12 km por litro (km/L).
#
# Para isso, ele fornecerá:
# - O tempo gasto na viagem (em horas)
# - A velocidade média durante a viagem (em km/h)
#
# Com esses dados, podemos calcular:
# - A distância total percorrida: distância = tempo × velocidade
# - A quantidade de combustível gasta: litros = distância / 12

# Entrada:
# - Dois números inteiros:
#   1. Tempo gasto na viagem (em horas)
#   2. Velocidade média (em km/h)

# Saída:
# - Quantidade de litros de combustível necessários, com 3 casas decimais

# Exemplos de Entrada e Saída:
# +--------+--------------------+
# | Entrada |     Saída         |
# +--------+--------------------+
# | 10      | 70.833             |
# | 85      |                    |
# ------------------------------
# | 2       | 15.333             |
# | 92      |                    |
# ------------------------------
# | 22      | 122.833            |
# | 67      |                    |
# +--------+--------------------+


tempo_gasto = int(input())
velocidade_media = int(input())

gasto_combustivel = (tempo_gasto*velocidade_media) / 12

print(f'{gasto_combustivel:.3f}')