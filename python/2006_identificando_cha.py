T = int(input())
RESPOSTA = input().split()
acertos = 0
numeros = []

for i in range(len(RESPOSTA)):
    numero_convertido = int(RESPOSTA[i])
    numeros.append(numero_convertido)
    

for i in range(len(numeros)):
    if numeros[i] == T:
        acertos += 1
        
print(acertos)