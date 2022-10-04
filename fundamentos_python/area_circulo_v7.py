from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


def help():  # nesse caso não é necessário passar como parâmetro
    print('É necessário informar o raio do circulo')
    print(f'Sintaxe: {sys.argv[0]} <raio> ')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('A área do circulo é:', area)
