# Descrição:
# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa uma quantia monetária.
# O objetivo é calcular o menor número possível de notas e moedas necessárias
# para compor esse valor, utilizando as seguintes denominações:

# Notas disponíveis:
# - R$ 100.00
# - R$ 50.00
# - R$ 20.00
# - R$ 10.00
# - R$ 5.00
# - R$ 2.00

# Moedas disponíveis:
# - R$ 1.00
# - R$ 0.50
# - R$ 0.25
# - R$ 0.10
# - R$ 0.05
# - R$ 0.01

# Entrada:
# - Um único valor decimal N (0 ≤ N ≤ 1000000.00), com ponto como separador decimal.

# Saída:
# - Imprima a quantidade de cada nota e moeda necessárias para compor o valor,
#   no seguinte formato:
#
# NOTAS:
# x nota(s) de R$ 100.00
# x nota(s) de R$ 50.00
# ...
# MOEDAS:
# x moeda(s) de R$ 1.00
# x moeda(s) de R$ 0.50
# ...

# Observações:
# - Use ponto (.) como separador decimal, conforme padrão internacional.
# - O valor de saída deve mostrar todas as denominações, mesmo se a quantidade for zero.

# Exemplos de Entrada e Saída:
#
# Entrada:
# 576.73
# Saída:
# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01


cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

valor = float(input())
valor_centavos = round(valor * 100)

print("NOTAS:")
for nota in cedulas:
    nota_centavos = int(nota * 100)
    qtd = valor_centavos // nota_centavos
    valor_centavos %= nota_centavos
    print(f"{qtd} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for moeda in moedas:
    moeda_centavos = int(round(moeda * 100))
    qtd = valor_centavos // moeda_centavos
    valor_centavos %= moeda_centavos
    print(f"{qtd} moeda(s) de R$ {moeda:.2f}")
