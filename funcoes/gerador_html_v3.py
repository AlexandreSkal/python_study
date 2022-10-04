from operator import truediv


def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):  # parâemtro packing
    lista = ''.join((f'<li>{item}</li>' for item in itens))  # generator
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', False))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('Falhou', classe='error'))
    print(tag_bloco(tag_lista('item1', 'item2'), classe='info'))
