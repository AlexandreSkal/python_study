from datetime import datetime
from loja import Cliente, Vendedor, Compra, Lojas

def main():
    cliente = Cliente('Maria Lima ', 44)
    cliente2 = Cliente('Clara Rosa ', 22)
    vendedor = Vendedor('Pedro Geraldo', 36, 5000)
    compra1 = Compra(vendedor, datetime.now(), 512)
    compra2 = Compra(vendedor, datetime(2018, 6, 4), 256)
    cliente.registrar_compras(compra1)
    cliente.registrar_compras(compra2)
    print(f'Cliente: {cliente}',' (adulto)' if cliente.is_adult() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print (f'Total: {valor_total} em {qtde_compras} compras')
    print (f'Ultima compra: {cliente.get_data_ultima_compra()}')

    loja = Lojas(cliente, vendedor)
    loja.add_cliente(cliente2)
    loja.add_cliente(cliente)
    todos_clientes = loja.clientes
    print(todos_clientes[0])


if __name__ == '__main__':
    main()