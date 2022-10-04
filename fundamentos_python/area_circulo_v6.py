from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o Raio: ')
    area = circulo(raio)
    print('A área do circulo é:', area)
