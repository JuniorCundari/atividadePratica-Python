# Exercício 1

r = 's'
while r == 's':
    nome = str(input('Nome do aluno: '))
    nota = float(input('Nota final: '))
    for i in range(1):
        if nota <= 2.9:
            con = 'E'
            print('O aluno {} tirou nota {} e se enquadra no conceito {}'.format(nome, nota, con))
        elif nota <= 4.9:
            con = 'D'
            print('O aluno {} tirou nota {} e se enquadra no conceito {}'.format(nome, nota, con))
        elif nota <= 6.9:
            con = 'C'
            print('O aluno {} tirou nota {} e se enquadra no conceito {}'.format(nome, nota, con))
        elif nota <= 8.9:
            con = 'B'
            print('O aluno {} tirou nota {} e se enquadra no conceito {}'.format(nome, nota, con))
        elif nota <= 10:
            con = 'A'
            print('O aluno {} tirou nota {} e se enquadra no conceito {}'.format(nome, nota, con))
# Caso o usuário digite uma nota maior que 10, imprimira a 'Nota inválida'
        else:
            print('Nota inválida!')
    r = str(input('Inserir dados? [s/n] '))
