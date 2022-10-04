# 0, 1, 1, 2, 3, 5, 8, 11, 21....

def fibonacci(limite):
    resultado = [0, 1]
    for _ in range(2, limite):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fibo in fibonacci(5):
        print(fibo)
