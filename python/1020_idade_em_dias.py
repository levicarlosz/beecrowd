# Descrição:
# Leia um valor inteiro que representa a idade de uma pessoa em dias,
# e converta esse valor para anos, meses e dias.

# Regras para o cálculo:
# - Considere que:
#     - 1 ano tem 365 dias
#     - 1 mês tem 30 dias
# - Não é necessário considerar anos bissextos ou meses com dias diferentes.
# - Nunca haverá casos como 360, 363 ou 364 dias (para evitar 12 meses + dias).

# Entrada:
# - Um valor inteiro N (representando a idade em dias)

# Saída:
# - A saída deve conter:
#     N_anos ano(s)
#     N_meses mes(es)
#     N_dias dia(s)

# Exemplo de Entrada e Saída:
# +---------+-------------------------+
# | Entrada |        Saída           |
# +---------+-------------------------+
# | 400     | 1 ano(s)                |
# |         | 1 mes(es)               |
# |         | 5 dia(s)                |
# |---------|-------------------------|
# | 800     | 2 ano(s)                |
# |         | 2 mes(es)               |
# |         | 10 dia(s)               |
# |---------|-------------------------|
# | 30      | 0 ano(s)                |
# |         | 1 mes(es)               |
# |         | 0 dia(s)                |
# +---------+-------------------------+


N = int(input())

DIAS_ANO = 365
DIAS_MESES = 30

idade_anos = N // DIAS_ANO
idade_meses = (N % DIAS_ANO) // DIAS_MESES 
idade_dias = (N % DIAS_ANO) % DIAS_MESES

print(f'{idade_anos} ano(s)')
print(f'{idade_meses} mes(es)')
print(f'{idade_dias} dia(s)')