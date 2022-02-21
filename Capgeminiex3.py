# o algoritmo utiliza uma estrutura de dados comum chamada Dicionário
from collections import defaultdict

# primeiramente, o algortimo recebe a palavra que será analisada para identificação dos anagramas
word = str(input('Informe a palavra que será analisada: '))

# as variáveis da quantidade de letras, e de repetições, são inicializadas
qtde_letras = 0
repeticoes = defaultdict(int)

# para cada letra da palavra informada, o algoritmo contabiliza 1 letra para a palavra, e 1 repetição para cada letra
# note que, na estrutura de dados do tipo Dicionário, uma string (no caso, a letra) é o índice do "vetor"
for letra in word:
    qtde_letras += 1
    repeticoes[letra] += 1

# a fórmula para cálculo de anagramas é uma fração
# na parte superior da fração (numerador), calcula-se o fatorial da quantidade de letras da palavra
numerador = 1
for i in range(qtde_letras,0,-1):
    numerador = numerador * i

# na parte inferior da fração (denominador), multiplica-se as fatoriais das quantidades repetidas por letra (considerando somente as letras repetidas)
denominador = 1
for letra in repeticoes:
    for j in range(repeticoes[letra],0,-1):
        denominador = denominador * j

# após dividir o numerador pelo denominador, retira-se 1 unidade (para não contar a própria palavra inserida)
qtde_anagramas = numerador / denominador - 1
print(qtde_anagramas)