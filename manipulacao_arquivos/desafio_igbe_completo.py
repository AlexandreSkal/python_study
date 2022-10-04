import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando CSV...')
        dados = entrada.read().decode('latin1')
        print('Download completo!!!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'Coluna 4: {cidade[8]}, Coluna 9: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
