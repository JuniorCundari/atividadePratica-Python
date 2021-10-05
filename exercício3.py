#Exercício 3

import random

lista = []

def doadores(nome:str, doacao:float):
    lista.extend(((nome + ' ') * int(doacao // 10)).split())
    return

def sorteado():
    random.shuffle(lista)
    print(f'Nomes embaralhados: {lista}')
    return random.choice(lista)

# Programa Principal
opcao = int(input('Deseja cadastrar doador? 0 - Não     1 - Sim '))
while opcao == 1:
    doador = input('Qual o nome do doador? ')
    valor = float(input('Qual o valor da doação? '))
    while (len(doador.strip()) == 0) or (valor < 10):
        print('Nenhum nome foi digitado, valor mínimo para doação é R$ 10')
        doador = input('Digite o nome do doador: ')
        valor = float(input('Qual o valor da doação? '))
    doadores(doador, valor)
    opcao = int(input('Deseja cadastrar doador? 0 - Não     1 - Sim '))

# Se o usuário cadastrou algum doador será imprimido a lista e o vencedor do sorteio
if len(lista) > 0:
    print(f'Lista dos doares que participaram do sorteio: {lista}')
    print(f'O vencedor(a) do sorteio: {sorteado()}')
