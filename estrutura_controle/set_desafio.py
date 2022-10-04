PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    # consigo passar o lower e split direto no set e fazer a interseção direto em um unico dogido
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui pelo menos uma palavra proíbida: ', intersecao)
    else:
        print('Texto autorizado: ', texto)
