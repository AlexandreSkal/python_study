from pickletools import read_uint1
from .pessoa import Pessoa


def get_data(compra):
    return compra.data

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compras(self, compras):
        self.compras.append(compras)

    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=get_data)[-1].data
            #com lambda
            # sorted(self.compra, key=lambda c: c.data)[-1].data

    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total