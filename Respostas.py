
""" PERGUNTA 1 - Resposta vai ser 91 """

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

""" PERGUNTA 2 - Sequencia Fibonacci"""

num = int(input("Digite um número inteiro: "))

a, b = 0, 1
while b < num:
    a, b = b, a + b

if b == num:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

""" PERGUNTA 3 - 

a) 1, 3, 5, 7, 9 - A lógica é adicionar 2 ao número anterior.

b) 2, 4, 8, 16, 32, 64, 128 - A lógica é multiplicar o número anterior por 2.

c) 0, 1, 4, 9, 16, 25, 36, 49 - A lógica é elevar o índice do termo na sequência ao quadrado.

d) 4, 16, 36, 64, 100 - A lógica é adicionar sucessivamente os números ímpares (3, 5, 7, ...).

e) 1, 1, 2, 3, 5, 8, 13 - A lógica é a soma dos dois números anteriores da sequência.

f) 2, 10, 12, 16, 17, 18, 19, 20 - A lógica é adicionar 8, 2, 4, 1, 1, 1, sucessivamente aos termos anteriores.

"""

# Definindo a sequência A
seq = [1, 3, 5, 7]

# Obtendo o próximo número da sequência
prox_num = seq[-1] + 2

# Imprimindo o próximo número
print(prox_num)

##############

# Definindo a sequência B
seq = [2, 4, 8, 16, 32, 64]

# Obtendo o próximo número da sequência
prox_num = seq[-1] * 2

# Imprimindo o próximo número
print(prox_num)

##############

# Definindo a sequência C
seq = [0, 1, 4, 9, 16, 25, 36]

# Obtendo o próximo número da sequência
prox_num = (len(seq)) ** 2

# Imprimindo o próximo número
print(prox_num)

##############

# Definindo a sequência D
seq = [4, 16, 36, 64]

# Obtendo o próximo número da sequência
prox_num = seq[-1] + ((len(seq) * 2) + 1)

# Imprimindo o próximo número
print(prox_num)

##############

# Definindo a sequência E
seq = [1, 1, 2, 3, 5, 8]

# Obtendo o próximo número da sequência
prox_num = seq[-1] + seq[-2]

# Imprimindo o próximo número
print(prox_num)

##############

# Definindo a sequência F
seq = [2, 10, 12, 16, 17, 18, 19]

# Obtendo o próximo número da sequência
prox_num = seq[-1] + [8, 2, 4, 1, 1, 1][len(seq) % 6]

# Imprimindo o próximo número
print(prox_num)


""" PERGUNTA 4 - Carro a Ribeirão Preto """

distancia = 100 # em km
vel_carro = 110 # em km/h
vel_caminhao = 80 # em km/h

tempo_encontro = distancia / (vel_carro + vel_caminhao) # em horas

posicao_carro = vel_carro * tempo_encontro # em km
posicao_caminhao = distancia - posicao_carro # em km

if posicao_carro < posicao_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

""" PERGUNTA 5 - STRING """

# Recebe a string do usuário
string = input("Digite uma string para inverter: ")

# Inicializa a string invertida
string_invertida = ""

# Loop que percorre a string de trás para frente, adicionando cada caracter à string invertida
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprime a string invertida
print("A string invertida é:", string_invertida)