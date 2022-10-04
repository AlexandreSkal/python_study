import csv

with open('desafio-ibge.csv') as dados_ibge:
    for dados in csv.reader(dados_ibge):
        print(f'Coluna 4: {dados[3]}, Coluna 9: {dados[8]}')
