MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""


MENU_RELATORIOS = """Relatórios
1 - Relatório de Ordem de Serviços
2 - Relatório de Peças Utilizadas 
0 - Sair
"""


MENU_ENTIDADES = """Entidades
1 - ORDEM DE SERVIÇO
2 - CLIENTES
3 - TECNICO
4 - PEÇAS
5 - PEÇAS UTILIZADAS
"""


QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_timeint=3)
    import os
    from time import sleep
    sleep(wait_time)
    os.system(clear)