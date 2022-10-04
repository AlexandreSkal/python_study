class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 10
d1.ano = 2022
print(d1)

d1 = Data()
d1.dia = 15
d1.mes = 11
d1.ano = 2022
print(d1)
