# 0, 1, 1, 2, 3, 5, 8, 11, 21....

def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fibo in fibonacci(5):
        print(fibo)
