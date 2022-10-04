# exemplo utilizando o with, forma simples e segura de garantir o fechamento do arquivo
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
if arquivo.closed:
    print('Arquivo fechado!')
