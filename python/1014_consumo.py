# Descrição:
# Calcule o consumo médio de um automóvel, fornecidos:
# - a distância total percorrida (em Km), e
# - o total de combustível gasto (em litros).

# Entrada:
# O programa deve ler dois valores:
# - Um valor inteiro X: distância total percorrida (Km)
# - Um valor real Y: total de combustível gasto (litros), com 1 casa decimal

# Saída:
# O programa deve imprimir o consumo médio do automóvel, com:
# - 3 casas decimais
# - seguido da unidade: "km/l"
# Exemplo de saída: 14.286 km/l


# Exemplos de Entrada e Saída:
# +-------------------+------------------+
# | Entrada           | Saída            |
# +-------------------+------------------+
# | 500               | 14.286 km/l      |
# | 35.0              |                  |
# |-------------------|------------------|
# | 2254              | 18.119 km/l      |
# | 124.4             |                  |
# |-------------------|------------------|
# | 4554              | 9.802 km/l       |
# | 464.6             |                  |
# +-------------------+------------------+

distancia = int(input())
combustivel = float(input())

consumo_medio = distancia / combustivel

print(f'{consumo_medio:.3f} km/l')