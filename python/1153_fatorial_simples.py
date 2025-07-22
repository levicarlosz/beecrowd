# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

# Entrada
# A entrada contém um valor inteiro N (0 < N < 13).

# Saída
# A saída contém um valor inteiro, correspondente ao fatorial de N.

N = int(input())

primeiro_numero = N
decremento = 1
if N != 0:
    while decremento < N:
        multiplicador = N - decremento
        primeiro_numero = primeiro_numero * multiplicador
        decremento += 1

print(primeiro_numero)