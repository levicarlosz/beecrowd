# começa e termina com 1
# apenas os numeros 1 e 2 aparecem
# numero 2 aparece pelo menos uma vez

sequencia = []
qtd_sequencias = 0
i = 0

tamanho_sequencia = int(input())

while i <= tamanho_sequencia - 1:
    numero = int(input())

    valor_valido = True if numero == 1 or numero == 2 else False

    if 1 <= numero and numero <= tamanho_sequencia and valor_valido:
            sequencia.append(numero)
            i += 1


for i in range(len(sequencia) - 1):
    atual = sequencia[i]
    proximo = sequencia[i + 1]

    if atual != proximo:
        qtd_sequencias += 1

valor = qtd_sequencias + 1

print(valor)
