from http.server import executable


def executar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('bom dia')


def boa_tarde():
    print('boa tarde')


if __name__ == '__main__':
    executar(boa_tarde)
    executar(bom_dia)
    executar(1)
