# Descrição:
# Degustação de chá às escuras é a habilidade de identificar um chá apenas usando
# os sentidos do olfato e paladar.
#
# Durante uma competição, um tipo de chá é preparado (com código de 1 a 4):
# (1) chá branco, (2) chá verde, (3) chá preto, (4) chá de ervas.
#
# Cinco competidores recebem uma xícara e tentam adivinhar qual o tipo do chá.
# Cada um dá uma resposta (um número entre 1 e 4).
#
# Objetivo:
# Determinar quantos dos cinco competidores acertaram o tipo do chá.

# Entrada:
# - A primeira linha contém um inteiro T (1 ≤ T ≤ 4), representando o tipo real do chá.
# - A segunda linha contém cinco inteiros (A, B, C, D, E), representando a resposta de cada competidor.

# Saída:
# - Um único inteiro, representando o número de respostas corretas.

# Exemplo de Entrada e Saída:
# +-----------+---------------------+
# | Entrada   | Saída               |
# +-----------+---------------------+
# | 1         | 2                   |
# | 1 2 3 2 1 |                     |
# |-----------|---------------------|
# | 3         | 0                   |
# | 4 1 1 2 1 |                     |
# +-----------+---------------------+

T = int(input())
RESPOSTA = input().split()
acertos = 0
numeros = []

for i in range(len(RESPOSTA)):
    numero_convertido = int(RESPOSTA[i])
    numeros.append(numero_convertido)
    

for i in range(len(numeros)):
    if numeros[i] == T:
        acertos += 1
        
print(acertos)