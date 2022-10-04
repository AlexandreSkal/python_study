class Carro():
    def __init__(self, velocidade):
        self.velocidade = velocidade

    def acelerar(self, delta=5):

        if self.velocidade > 180:
            self.velocidade = 180
        elif self.velocidade <= 180-delta:
            self.velocidade += delta
        else:
            self.velocidade = 180
        return self.velocidade

    def freiar(self, delta=5):
        if self.velocidade >= 0 + delta:
            self.velocidade -= delta
        elif self.velocidade < 0:
            self.velocidade = 0
        else:
            self.velocidade = 0
        return self.velocidade


if __name__ == '__main__':
    c1 = Carro(10)

    for _ in range(45):
        print(c1.acelerar())

    for _ in range(10):
        print(c1.freiar(delta=1))
