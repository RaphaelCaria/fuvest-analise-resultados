# entrada = open ('fuvest2fase_2022.txt', 'r')
# saida = open ('fuvestdel.txt', 'w')

# for line in entrada:
#     if line.find('...') > 0:
#         camp = line.split('...')
#         saida.write(f'{camp[0]};{camp[1]}\n')
# from os import system, name

# system('cls') if (name == 'nt') else system('clear')

# for ano in range(2024, 1998, -1):
#     with open(f'fuvest_py/fuvest_chamada/fuvest_{ano}_chamada_1.txt', 'r', encoding= 'utf=8') as entrada:
#         with open('fuvest_chamada_ano.csv', 'a', encoding= 'utf=8') as saida:  # Abrir no modo de escrita anexada ('a')
#             for col in entrada:
#                 if len(col) > 14:
#                     if col[-4] == '−' or col[-4] == '-':
#                         nome = col[:-16]
#                         cpf = col[-15:-8]
#                         curso = col[-7:]
#                         saida.write(f'{nome};{cpf};{curso}\n')  # Adicionar '\n' para nova linha

from os import system, name
import codecs

system('cls') if (name == 'nt') else system('clear')

def abrir_arquivo(filename, codificacoes):
    for codificacao in codificacoes:
        try:
            return codecs.open(filename, 'r', encoding=codificacao)
        except UnicodeDecodeError:
            continue
    raise ValueError(f'Nenhuma das codificações {codificacoes} funcionou para abrir o arquivo {filename}')

codificacoes_possiveis = ['utf-8', 'latin1']  # Adicione outras codificações se necessário

for ano in range(2024, 1998, -1):
    with abrir_arquivo(f'fuvest_py/fuvest_chamada/fuvest_{ano}_chamada_1.txt', codificacoes_possiveis) as entrada:
        with open('fuvest_chamada_ano.csv', 'a', encoding='utf-8') as saida:
            for col in entrada:
                if len(col) > 14:
                    if col[-4] == '−' or col[-4] == '-':
                        nome = col[:-16]
                        cpf = col[-15:-8]
                        curso = col[-7:]
                        saida.write(f'{nome};{cpf};{curso}\n')
