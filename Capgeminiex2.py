import re

password = input(str('Informe a senha desejada: '))

flag = 0
while True:
    if (len(password)<6):
        flag = - 1
        print(f'A senha informada contém {(len(password))} caracteres, informe uma senha com pelo menos 6 caracteres')
        print(f'Adcione mais {(len(password) - 6)} caracteres.')
        break
    elif not re.search("[a-z]", password):
        print('A senha deve conter letras minusculas.')
        flag = - 1
        break
    elif not re.search('[A-Z]', password):
        print('A senha deve conter letras maiúsculas.')
        flag = - 1
        break
    elif not re.search('[0-9]', password):
        print('A senha deve conter pelo menos um número.')
        flag = - 1
        break
    elif not re.search('[!@#$%^&*()-+]', password):
        print('A senha deve conter pelo menos um caractere especial !@#$%^&*()-+')
        flag = - 1
        break
    elif re.search('\s', password):
        print('A senha não pode conter espaços.')
        flag = - 1
        break
    else:
        flag = 0
        print('Senha válida!')
        break
if flag == - 1:
    print('Senha fraca')



