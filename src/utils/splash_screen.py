from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_ordem_servico = config.QUERY_COUNT.format(tabela="ordem_servico")
        self.qry_tecnico = config.QUERY_COUNT.format(tabela="tecnico")
        self.qry_peca = config.QUERY_COUNT.format(tabela="peca")
        self.qry_pecas_utilizadas = config.QUERY_COUNT.format(tabela="pecas_utilizadas")
        self.qry_clientes = config.QUERY_COUNT.format(tabela="clientes")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Artur Hollanda, Bernardo Rocha, Pablo Moura, Julio Sepulcri e Olívia Noronha"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_ordem_servico(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_ordem_servico)["total_ordem_servico"].values[0]

    def get_total_tecnico(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_tecnico)["total_tecnico"].values[0]

    def get_total_peca(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_peca)["total_peca"].values[0]

    def get_total_pecas_utilizadas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_pecas_utilizadas)["total_pecas_utilizadas"].values[0]

    def get_total_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_clientes)["total_clientes"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - ORDEM DE SERVIÇO:         {str(self.get_total_ordem_servico()).rjust(5)}
        #      2 - TÉCNICO:         {str(self.get_total_tecnico()).rjust(5)}
        #      3 - PEÇA:     {str(self.get_total_peca()).rjust(5)}
        #      4 - PEÇAS UTILIZADAS:          {str(self.get_total_pecas_utilizadas()).rjust(5)}
        #      5 - CLIENTES: {str(self.get_total_clientes()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """