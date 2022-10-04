def funcao_sortear():
    from random import randint
    return randint(1, 6)


if __name__ == '__main__':
    sorteado = funcao_sortear()

    print(f'O valor sorteado foi {sorteado}')
    for i in range(1, 7):
        valor_digitado = input(f'Digite um valor, é sua {i}° chance: ')
        if sorteado % 2 != 0:
            print('é impar')
            continue
        elif sorteado == valor_digitado:
            print('Acertou')
            break
        else:
            print('não acertou')
