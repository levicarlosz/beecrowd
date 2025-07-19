valores = input().split()
numeros = []

for valor in valores:
    valor = int(valor)
    numeros.append(valor)


for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            
            
for numero in numeros:
    print(numero)
    
print("")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])

### Escrevi o código acima porem nao foi assim que o beecrowd aceitou abaixo vai como ele aceita

valores = input().split()
numeros = []

for valor in valores:
    valor = int(valor)
    numeros.append(valor)


for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            
            
for numero in numeros:
    print(numero)
    
print("")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])

