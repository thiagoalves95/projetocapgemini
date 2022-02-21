from collections import defaultdict

password = input(str('Informe a senha desejada: '))

qtde_letras = 0
repeticoes = defaultdict(int)

for letra in password:
    qtde_letras += 1
    repeticoes[letra] += 1

numerador = 1
for i in range(qtde_letras,0,-1):
    numerador = numerador * i

denominador = 1
for letra in repeticoes:
    for j in range(repeticoes[letra],0,-1):
        denominador = denominador * j

qtde_anagramas = (numerador / denominador) - 1
print(qtde_anagramas)