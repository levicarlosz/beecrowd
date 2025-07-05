# Descrição:
# Escreva um programa que leia:
# - o número de um funcionário (inteiro)
# - o número de horas trabalhadas por ele (inteiro)
# - o valor que recebe por hora (ponto flutuante com duas casas decimais)
#
# Em seguida, calcule o salário do funcionário e exiba:
# - o número do funcionário
# - o salário com exatamente duas casas decimais

# Entrada:
# O programa deve ler:
# - 2 números inteiros: número do funcionário e horas trabalhadas
# - 1 número decimal (duas casas): valor por hora

# Saída:
# Imprima:
# - "NUMBER = X", onde X é o número do funcionário
# - "SALARY = U$ Y", onde Y é o salário calculado, com duas casas decimais
# Atenção: Deve haver um espaço em branco antes e depois do sinal de igualdade,
# e um espaço após o cifrão ($). Finalize a saída com uma quebra de linha.

# Fórmula:
# SALARY = horas_trabalhadas × valor_por_hora

# Exemplos de Entrada e Saída:
# +--------------------------+-------------------------+
# | Entrada                  | Saída                   |
# +--------------------------+-------------------------+
# | 25 100 5.50              | NUMBER = 25             |
# |                          | SALARY = U$ 550.00      |
# |--------------------------|-------------------------|
# | 1 200 20.50              | NUMBER = 1              |
# |                          | SALARY = U$ 4100.00     |
# |--------------------------|-------------------------|
# | 6 145 15.55              | NUMBER = 6              |
# |                          | SALARY = U$ 2254.75     |
# +--------------------------+-------------------------+


numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print(f"NUMBER = {numero_funcionario}" + f"SALARY = U$ {salario:.2f}") # <-- dessa forma apresenta Presentation Error basta usar duas funcoes print
