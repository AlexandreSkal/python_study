# exemplo utilizando o with, forma simples e segura de garantir o fechamento do arquivo
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
if arquivo.closed:
    print('Arquivo fechado!')
