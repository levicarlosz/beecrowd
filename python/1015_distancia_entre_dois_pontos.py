# Descrição:
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano:
# - ponto p1 com coordenadas (x1, y1)
# - ponto p2 com coordenadas (x2, y2)
#
# Calcule a distância entre esses dois pontos usando a fórmula da distância euclidiana:
#
# Distância = √((x2 - x1)² + (y2 - y1)²)

# Obs: use 4 casas decimais no resultado.

# Entrada:
# - A primeira linha contém dois números de ponto flutuante: x1 e y1
# - A segunda linha contém dois números de ponto flutuante: x2 e y2

# Saída:
# - Imprima a distância calculada com 4 casas decimais

# Exemplos de Entrada e Saída:
# +-------------------+-----------+
# | Entrada           | Saída     |
# +-------------------+-----------+
# | 1.0 7.0           | 4.4721    |
# | 5.0 9.0           |           |
# |-------------------|-----------|
# | -2.5 0.4          | 16.1484   |
# | 12.1 7.3          |           |
# |-------------------|-----------|
# | 2.5 -0.4          | 16.4575   |
# | -12.2 7.0         |           |
# +-------------------+-----------+



p1 = input().split()
p2 = input().split()


X1 = float(p1[0])
Y1 = float(p1[1])

X2 = float(p2[0])
Y2 = float(p2[1])

distancia = (((X2 - X1) ** 2) + ((Y2 - Y1)**2)) ** 0.5

print(f"{distancia:.4f}")