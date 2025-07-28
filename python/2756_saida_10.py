# Coloque sete espaços em branco e coloque o carácter 'A';
# Coloque seis espaços em branco e coloque o carácter 'B', um espaço em branco e o carácter 'B';
# Coloque cinco espaços em branco e coloque o carácter 'C', três espaço em branco e o carácter 'C';
# Coloque quatro espaços em branco e coloque o carácter 'D', cinco espaço em branco e o carácter 'D';
# Coloque três espaços em branco e coloque o carácter 'E', sete espaço em branco e o carácter 'E';

def pular_espacos(qtd:int, letra:str, espacamento:int):
    margem = " " * qtd
    
    espacamento_entre_linhas = " " * espacamento
    
    if espacamento == 0:
        linha = margem + letra
    else:
        linha = margem + letra + espacamento_entre_linhas + letra
    return linha
    
    
print(pular_espacos(7, "A", 0))

print(pular_espacos(6, "B", 1))
print(pular_espacos(5, "C", 3))
print(pular_espacos(4, "D", 5))
print(pular_espacos(3, "E", 7))

print(pular_espacos(4, "D", 5))
print(pular_espacos(5, "C", 3))
print(pular_espacos(6, "B", 1))
print(pular_espacos(7, "A", 0))