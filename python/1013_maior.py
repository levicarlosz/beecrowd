# Descrição:
# Faça um programa que leia três valores inteiros e apresente o maior dos três,
# seguido da mensagem: "eh o maior".

# Dica:
# Utilize a seguinte fórmula para encontrar o maior entre dois números:
#   maiorAB = (a + b + abs(a - b)) / 2
# Essa fórmula retorna o maior entre 'a' e 'b'.
# Depois, compare o resultado com o terceiro número 'c' para encontrar o maior entre os três.

# Entrada:
# O programa deve ler três valores inteiros separados por espaço: A, B e C.

# Saída:
# O programa deve imprimir o maior dos três valores, seguido da frase:
#   "eh o maior"
# Exemplo: 106 eh o maior
# (Com um espaço entre o número e a mensagem)

# Exemplos de Entrada e Saída:
# +----------------------+------------------------+
# | Entrada              | Saída                  |
# +----------------------+------------------------+
# | 7 14 106             | 106 eh o maior         |
# |----------------------|------------------------|
# | 217 14 6             | 217 eh o maior         |
# +----------------------+------------------------+


entrada = input().split()

A = int(entrada[0])
B = int(entrada[1])
C = int(entrada[2])

MAIOR_AB = (A + B + abs(A - B)) / 2
MAIOR = int((C + MAIOR_AB + abs(C - MAIOR_AB)) / 2)


print(f"{MAIOR} eh o maior")