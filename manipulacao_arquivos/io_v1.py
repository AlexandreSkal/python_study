arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():  # quebra o  csv em linhas

    # separa os texto de cada linha usando a , usa o operador * para passar cada texto para os respectivos {}
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
