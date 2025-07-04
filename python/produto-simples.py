# Descrição:
# Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores 
# e atribua esta operação à variável PROD. Em seguida, mostre a variável PROD com 
# a mensagem correspondente.

# Entrada:
# O programa deve ler dois valores inteiros a partir da entrada padrão.

# Saída:
# Imprima a mensagem "PROD" seguida de um espaço, um sinal de igual com espaços 
# antes e depois, e o valor da variável PROD. Finalize a saída com uma quebra de linha. 
# Atenção: não incluir a quebra de linha pode resultar em “Presentation Error”.


# Exemplos de Entrada e Saída:
# -----------------------------
# Entrada         | Saída
# --------------- | ---------------
# 3  9            | PROD = 27
# -30 10          | PROD = -300
# 0  9            | PROD = 0


a = int(input())
b = int(input())
PROD = a * b

print(f"PROD = {PROD}")