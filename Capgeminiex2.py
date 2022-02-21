# o algoritmo importa uma biblioteca para utilizar expressões regulares, e assim encontrar determinado tipo de caractere na string informada
import re

# primeiramente, o algoritmo recebe a senha que será validada
password = str(input('Informe a senha desejada: '))

# inicializa a variável que guarda a quantidade de regras de validação não atendidas
# antes de iniciar a análise, dizemos que nenhuma regra foi atendida (até esse momento)
qtde_validacoes_nao_atendidas = 4

# o algoritmo verifica se há ao menos 1 digito na string informada; se houver, esse critério foi atendido
if re.search('[0-9]', password):
    qtde_validacoes_nao_atendidas -= 1

# o algoritmo verifica se há ao menos 1 letra minúscula na string informada; se houver, esse critério foi atendido
if re.search("[a-z]", password):
    qtde_validacoes_nao_atendidas -= 1

# o algoritmo verifica se há ao menos 1 letra maiúscula na string informada; se houver, esse critério foi atendido
if re.search('[A-Z]', password):
    qtde_validacoes_nao_atendidas -= 1

# o algoritmo verifica se há ao menos 1 caractere especial na string informada; se houver, esse critério foi atendido
if re.search('[!@#$%^&*()-+]', password):
    qtde_validacoes_nao_atendidas -= 1

# caso a senha informada tenha menos de 6 caracteres, e a diferença para chegar a 6 caracteres é maior que a quantidade de validações não atendidas, essa diferença para chegar a 6 (que é o mínimo) passa a ser a quantidade mínima de caracteres necessárias
# caso contrário, a quantidade de caracteres necessários é a quantidade de validações não atendidas
if len(password) < 6 and (6 - len(password) > qtde_validacoes_nao_atendidas):
    qtde_caracteres_necessarios = 6 - len(password)
else:
    qtde_caracteres_necessarios = qtde_validacoes_nao_atendidas


print(qtde_caracteres_necessarios)