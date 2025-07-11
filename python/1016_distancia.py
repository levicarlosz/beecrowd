# Descrição:
# Dois carros (X e Y) partem na mesma direção:
# - Carro X com velocidade constante de 60 km/h
# - Carro Y com velocidade constante de 90 km/h
#
# A diferença de velocidade entre os dois é de 30 km/h.
# Isso significa que o carro Y se distancia 30 km do carro X a cada 60 minutos.
# Ou seja, Y se afasta 1 km a cada 2 minutos.

# Objetivo:
# Dada uma distância D (em km), calcule o tempo (em minutos) que o carro Y leva
# para abrir essa distância em relação ao carro X.

# Entrada:
# - Um único valor inteiro D (distância em quilômetros)

# Saída:
# - O tempo, em minutos, que o carro Y leva para abrir essa distância sobre o carro X

# Exemplos de Entrada e Saída:
# +-----------+--------+
# | Entrada   | Saída  |
# +-----------+--------+
# | 30        | 60     |
# |-----------|--------|
# | 110       | 220    |
# |-----------|--------|
# | 7         | 14     |
# +-----------+--------+


DISTANCIA = int(input())

tempo = DISTANCIA * 2

print(f'{tempo} minutos')