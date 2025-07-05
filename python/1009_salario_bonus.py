# Descrição:
# Faça um programa que leia:
# - o nome de um vendedor (apenas o primeiro nome, como string)
# - o salário fixo do vendedor (número com duas casas decimais)
# - o total de vendas efetuadas no mês (número com duas casas decimais)

# Sabendo que o vendedor recebe 15% de comissão sobre o valor total das vendas,
# calcule o total que ele deverá receber no final do mês, com duas casas decimais.

# Entrada:
# O programa deve ler:
# - 1 string: nome do vendedor
# - 2 números de ponto flutuante (double): salário fixo e total das vendas

# Saída:
# Imprima:
# - "TOTAL = R$ X", onde X é o valor total a receber, com duas casas decimais
# Atenção: Deve haver um espaço após o sinal de igual e após o cifrão.
# Finalize a saída com uma quebra de linha para evitar "Presentation Error".

# Exemplos de Entrada e Saída:
# +----------------------------+------------------------+
# | Entrada                   | Saída                  |
# +----------------------------+------------------------+
# | JOAO                      | TOTAL = R$ 684.54      |
# | 500.00                    |                        |
# | 1230.30                   |                        |
# |---------------------------|------------------------|
# | PEDRO                     | TOTAL = R$ 700.00      |
# | 700.00                    |                        |
# | 0.00                      |                        |
# |---------------------------|------------------------|
# | MANGOJATA                 | TOTAL = R$ 1884.58     |
# | 1700.00                   |                        |
# | 1230.50                   |                        |
# +----------------------------+------------------------+


NOME = input()
SALARIO_FIXO = float(input())
TOTAL_VENDAS = float(input())

SALARIO_BONUS = SALARIO_FIXO + (TOTAL_VENDAS * 0.15)

print(f"TOTAL = R$ {SALARIO_BONUS:.2f}")