# Descrição:
# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo
# em qual dos seguintes intervalos o valor se encontra:
# - [0,25]
# - (25,50]
# - (50,75]
# - (75,100]
#
# Observações:
# - O símbolo [ ou ] indica que o valor é incluído no intervalo (inclusivo).
# - O símbolo ( indica que o valor não é incluído (exclusivo).
#   Por exemplo: (25,50] inclui valores maiores que 25 até 50, incluindo o 50, mas não o 25.
#
# Caso o valor não esteja em nenhum desses intervalos, deverá ser exibida a mensagem:
# "Fora de intervalo".

# Entrada:
# - Um número de ponto flutuante qualquer.

# Saída:
# - Uma mensagem indicando em qual intervalo o número está,
#   ou "Fora de intervalo" se ele não estiver em nenhum dos quatro.

# Exemplos de Entrada e Saída:
# +-----------+----------------------+
# | Entrada   | Saída               |
# +-----------+----------------------+
# | 25.01     | Intervalo (25,50]    |
# |-----------|----------------------|
# | 25.00     | Intervalo [0,25]     |
# |-----------|----------------------|
# | 100.00    | Intervalo (75,100]   |
# |-----------|----------------------|
# | -25.02    | Fora de intervalo    |
# +-----------+----------------------+


entrada = float(input())

intervalo = ""

intervalos = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]

if entrada >= 0 and entrada <= 25.0000:
    intervalo = intervalos[0]
    print(f"Intervalo {intervalo}")
elif entrada > 25.0000 and entrada <= 50.0000:
    intervalo = intervalos[1]
    print(f"Intervalo {intervalo}")
elif entrada > 50.0000 and entrada <= 75.0000:
    intervalo = intervalos[2]
    print(f"Intervalo {intervalo}")
elif entrada > 75.0000 and entrada <= 100.0000:
    intervalo = intervalos[3]
    print(f"Intervalo {intervalo}")
else:
    intervalo = "Fora de intervalo"
    print(f"{intervalo}")



