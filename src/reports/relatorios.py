from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_ordem_servico.sql") as f:
            self.query_ordem_servico = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_pecas_utilizadas.sql") as f:
            self.query_relatorio_pecas_utilizadas = f.read()

    def get_relatorio_ordem_servico(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_ordem_servico))
        input("Pressione Enter para Sair do Relatório de Ordem de Serviço")

    def get_relatorio_pecas_utilizadas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_pecas_utilizadas))
        input("Pressione Enter para Sair do Relatório de Peças Utilizadas na Ordem de Serviço")