# Descrição:
# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que:
# - a nota A tem peso 3.5
# - a nota B tem peso 7.5
# A soma dos pesos é 11.
# Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

# Entrada:
# O programa deve ler 2 valores com uma casa decimal cada, representando as notas.

# Saída:
# Imprima a mensagem "MEDIA" seguida de um espaço, um sinal de igual com espaços
# antes e depois, e o valor da média calculada com **5 dígitos após o ponto decimal**.
# Finalize a saída com uma quebra de linha.
# Atenção: A ausência da quebra de linha pode causar “Presentation Error”.

# Tabela de Exemplos de Entrada e Saída:
# +-------------+------------------+
# | Entrada     | Saída            |
# +-------------+------------------+
# | 5.0 7.1     | MEDIA = 6.43182  |
# | 0.0 7.1     | MEDIA = 4.84091  |
# | 10.0 10.0   | MEDIA = 10.00000 |
# +-------------+------------------+

A = float(input()) * 3.5
B = float(input()) * 7.5
SOMA = A + B
MEDIA = SOMA / 11
print(f"MEDIA = {MEDIA:.5f}")
