def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 3, 6))

    # packing
    print(soma_n(2, 2))

    # unpacking
    tuple_nums = (1, 3, 4)
    print(soma_3(*tuple_nums))
    list_nums = [1, 2, 3]
    print(soma_3(*list_nums))
