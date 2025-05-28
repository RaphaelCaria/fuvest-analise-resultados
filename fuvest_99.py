with open('fuvest_1999_chamada_1.txt', 'r', encoding='utf-8') as entrada:
    saida = open('fuvest_sala2.csv', 'w', encoding='utf-8')
    for linha in entrada:
        if len(linha) >14:
            if linha[-4] == '−':
            # #if linha[-4] == chr(8722):
            #     nome = linha[:-16]
            #     cpf = linha[-15:-8]
            #     curso = linha[-7:]
            #     saida.write(f'{nome};{cpf};{curso}')
                campos = linha.rsplit(' ', 2)
                saida.write(';'.join(campos))