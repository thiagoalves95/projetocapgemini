n = int(input())
for i in range(0,n + 1):
    saida = ''
    qtd_espacos = n - i
    qtd_asteriscos = i

    for j in range(1, qtd_espacos+1):
        saida += ' '

    for i in range(1, qtd_asteriscos+1):
        saida += '*'

    print(saida)

