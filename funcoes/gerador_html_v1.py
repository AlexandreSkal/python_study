def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    #Testes (Assertions)
    assert tag_bloco('Incluído com sucesso') == \
        '<div class="success">Incluído com sucesso</div>'
    assert tag_bloco('Impossível inserir', 'error') == \
        '<div class="error">Impossível inserir</div>'
    print(tag_bloco('Bloco'))
