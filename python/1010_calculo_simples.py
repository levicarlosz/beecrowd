# Descrição:
# Neste problema, deve-se ler:
# - o código da peça 1 (inteiro)
# - o número de peças 1 (inteiro)
# - o valor unitário da peça 1 (float com 2 casas decimais)
# - o código da peça 2 (inteiro)
# - o número de peças 2 (inteiro)
# - o valor unitário da peça 2 (float com 2 casas decimais)

# Após a leitura, calcule e mostre o valor total a ser pago pelas duas peças.

# Entrada:
# A entrada contém duas linhas. Cada linha possui 3 valores:
# - código da peça (int)
# - quantidade de peças (int)
# - valor unitário (float com 2 casas decimais)

# Saída:
# A saída deve mostrar a mensagem:
# "VALOR A PAGAR: R$ X.XX"
# Onde X.XX é o valor total a ser pago, com duas casas decimais.
# Atenção:
# - Deve haver um espaço após os dois-pontos ":"
# - Deve haver um espaço após o símbolo "R$"
# - Finalize com uma quebra de linha para evitar "Presentation Error"

# Exemplos de Entrada e Saída:
# +------------------------+-------------------------------+
# | Entrada                | Saída                         |
# +------------------------+-------------------------------+
# | 12 1 5.30              | VALOR A PAGAR: R$ 15.50       |
# | 16 2 5.10              |                               |
# |------------------------|-------------------------------|
# | 13 2 15.30             | VALOR A PAGAR: R$ 51.40       |
# | 161 4 5.20             |                               |
# |------------------------|-------------------------------|
# | 1 1 15.10              | VALOR A PAGAR: R$ 30.20       |
# | 2 1 15.10              |                               |
# +------------------------+-------------------------------+

entrada_1 = input().split()
entrada_2 = input().split()

codigo_peca_1 = int(entrada_1[0])
qtd_pecas_1 = int(entrada_1[1])
valor_unitario_1 = float(entrada_1[2])

codigo_peca_2 = int(entrada_2[0])
qtd_pecas_2 = int(entrada_2[1])
valor_unitario_2 = float(entrada_2[2])

TOTAL = (qtd_pecas_1 * valor_unitario_1) + (qtd_pecas_2 * valor_unitario_2)

print(f"VALOR A PAGAR: R$ {TOTAL:.2f}")
