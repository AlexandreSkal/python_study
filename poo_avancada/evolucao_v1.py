class Humano():

    # Atributo da classe
    especie = 'Homo_Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = "Homo Neanderthalensis"
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn')
    grokn.das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Grokn.especie: {grokn.especie}')
    print(f'Jose.especie: {jose.especie}')
