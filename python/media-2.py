# Descrição:
# Leia 3 valores de ponto flutuante (A, B e C), que são as três notas de um aluno.
# A seguir, calcule a média ponderada do aluno, sabendo que:
# - A tem peso 2
# - B tem peso 3
# - C tem peso 5
# A soma dos pesos é 10.
# Considere que cada nota pode variar de 0 até 10.0, sempre com uma casa decimal.

# Entrada:
# O programa deve ler 3 valores com uma casa decimal (double), representando as notas A, B e C.

# Saída:
# Imprima a mensagem "MEDIA", seguida de um espaço, um sinal de igual com espaços antes e depois,
# e o valor da média ponderada com 1 dígito após o ponto decimal.
# Finalize a saída com uma quebra de linha.
# Atenção: A ausência da quebra de linha pode causar "Presentation Error".


# Exemplos de Entrada e Saída:
# +------------------+----------------+
# | Entrada          | Saída          |
# +------------------+----------------+
# | 5.0 6.0 7.0      | MEDIA = 6.3    |
# | 5.0 10.0 10.0    | MEDIA = 9.0    |
# | 10.0 10.0 5.0    | MEDIA = 7.5    |
# +------------------+----------------+

A = float(input()) * 2
B = float(input()) * 3
C = float(input()) * 5
 

MEDIA = (A + B + C) / 10

print(f"MEDIA = {MEDIA:.1f}")
