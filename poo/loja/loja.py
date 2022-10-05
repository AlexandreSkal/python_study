class Lojas():
    def __init__(self, cliente, vendedor):
        self.cliente = cliente
        self.vendedor = vendedor
        self.clientes = []
        self.vendedores = []

    def add_cliente(self, cliente):
        self.clientes.append(cliente)

    def add_vendedor(self, vendedor):
        self.vendedor.append(vendedor)
