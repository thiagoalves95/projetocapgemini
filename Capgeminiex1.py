# o algoritmo primeiramente solicita que o usuário informe a altura (quantidade de degraus) da escada
n = int(input("Digite a altura da escada: "))

# então, para cada degrau da escada (de 1 a N), o algoritmo identifica quantos espaços e asteriscos haverá em cada linha
for i in range(1,n+1):
    #primeiro, inicializa/limpa a variável que irá receber o texto a ser escrito na linha
    saida = ''
    #a quantidade de asteriscos será sempre o mesmo número da linha que está sendo escrita
    #exemplo: 1ª linha tem 1 asterisco, 2ª linha tem 2 asteriscos, e assim por diante
    qtd_asteriscos = i
    #a quantidade de espaços é igual ao número da linha menos o que ja estiver ocupado com asteriscos
    qtd_espacos = n - i

    #preenche a quantidade de espaços, à esquerda
    for j in range(1, qtd_espacos+1):
        saida += ' '

    #preenche a quantidade de asteriscos da linha, após os espaços
    for i in range(1, qtd_asteriscos+1):
        saida += '*'

    #imprime o conteúdo da linha
    print(saida)