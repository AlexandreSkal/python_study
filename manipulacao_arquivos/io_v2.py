arquivo = open('pessoas.csv')

# nesse exemplo os dados são lidos dinâmicamente  stream,
try:
    for registro in arquivo:

        # separa os texto de cada linha usando a , usa o operador * para passar cada texto para os respectivos {}
        # adicionamos strip para retirar espaços em brancos, podemos passar para o split oq queremos tirar tbm
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close
