def fim_semana(dia):
    dias_semana = {
        1: ['Domingo', 'fds'],
        2: ['Segunda', 'ds'],
        3: ['Terca', 'ds'],
        4: ['Quarta', 'ds'],
        5: ['Quinta', 'ds'],
        6: ['Sexta', 'ds'],
        7: ['Sabado', 'fds']
    }
    return dias_semana.get(dia, 'inválido')


for i in range(1, 8):
    dict_dias = fim_semana(i)
    if dict_dias[1] == 'fds':
        print(f'É final de semana: {dict_dias[0]}')
        continue
    else:
        print(f'É dia de semana: {dict_dias[0]}')
