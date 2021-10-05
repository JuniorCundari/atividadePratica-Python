# Exercício4

lista = []
from operator import itemgetter

def cadastroProduto(cadastrar: dict):
    lista.append(cadastrar)
    return

# Programa Principal
opcao = input('Você deseja cadastrar produtos? [s/n] ')
while opcao == 's':
    produto = {}
    produto['codigo'] = int(input('Qual é o código do produto? '))
# Se caso o usuário digitar 0 na coluna códigos o programa será encerrado
    if produto['codigo'] == 0:
        print('\nVocê digitou o CÓDIGO 0. Encerrando...')
        break
    produto['estoque'] = int(input('Qual é a quantidade atual do estoque? '))
    produto['minimo'] = int(input('Qual a quantidade mínima necessária do estoque? '))
    cadastroProduto(produto)
    print('-' * 55)
    opcao = input('Você deseja cadastrar produtos? [s/n] ')


if len(lista) > 0:
    print('\nProdutos em ordem crescente (código):')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))
    for listaOrdenada in sorted(lista, key=itemgetter('codigo')):
        print(str(listaOrdenada['codigo']).center(10), end='')
        print(str(listaOrdenada['estoque']).center(10), end='')
        print(str(listaOrdenada['minimo']).center(10))
else:
    print('Lista de produtos vazia.')
