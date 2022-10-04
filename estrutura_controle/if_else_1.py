# Conceito      Notas
# A             De 10,0 á 9,1
# A-            De 9,0 á 8,1
# B             De 8,0 á 7,1
# B-            De 7,0 á 6,1
# C             De 6,0 á 5,1
# C-            De 5,0 á 4,1
# D             De 4,0 á 3,1
# D-            De 3,0 á 2,1
# E             De 2,0 á 1,1
# E-            De 1,0 á 0,0

# Para notas maiore que 10 e menos que 0 será impresso nota inválida

from unicodedata import numeric


def conceito(nota):
    if type(nota == str):
        return str('não é um valor')
    elif nota > 10:
        return str('Valor inválido')
    elif nota >= 9.1:
        return str('A')
    elif nota >= 8.1:
        return str('A-')
    elif nota >= 7.1:
        return str('B')
    elif nota >= 6.1:
        return str('B-')
    elif nota >= 5.1:
        return str('C')
    elif nota >= 4.1:
        return str('C-')
    elif nota >= 3.1:
        return str('D')
    elif nota >= 2.1:
        return str('D-')
    elif nota >= 1.1:
        return str('E')
    elif nota >= 0.0:
        return str('E-')
    else:
        return str('Valor inválido')


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito_aluno = conceito(valor_informado)
    print(conceito_aluno)
