# Exercício 2

def criadorEmail(nome):
    sobrenome = str(input('Digite seu sobrenome: '))

    if sobrenome != '':
        ru = (input('Digite os últimos dois números do seu RU: '))
        if ru != '':
            novo_email = ((nome[0:2] + sobrenome + '{}' + ('@algoritmos.com.br')).format(ru))
            mensagem = 'Sr(a).'' ' + nome + ' ' + sobrenome + ', seu email é ' + (novo_email.lower())
            return mensagem
        else:
            print('Você digitou o RU inválido!')
    else:
        print('Sobrenome inválido')


# Programa Principal
nome = str(input('Digite seu nome: '))
if (len(nome) > 0):
    print(criadorEmail(nome))
else:
    print('Nome inválido, não foi possível gerar o email!')
