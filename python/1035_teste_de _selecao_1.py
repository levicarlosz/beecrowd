# Descrição:
# Leia 4 valores inteiros: A, B, C e D.
# A seguir, verifique se todos os seguintes critérios são atendidos:
# - B > C
# - D > A
# - (C + D) > (A + B)
# - C e D são positivos
# - A é par
#
# Se todos os critérios acima forem verdadeiros, imprimir:
# "Valores aceitos"
# Caso contrário, imprimir:
# "Valores nao aceitos"
#
# Entrada:
# - Quatro números inteiros A, B, C e D fornecidos em uma única linha ou em quatro linhas.
#
# Saída:
# - Uma única linha com a mensagem: "Valores aceitos" ou "Valores nao aceitos"
#
# Exemplos:
# Entrada:
# 5 6 7 8
# Saída:
# Valores nao aceitos
#
# Entrada:
# 2 3 2 6
# Saída:
# Valores aceitos


valores = input().split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

if B > C and D > A and (C + D) > (A+B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

