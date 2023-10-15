from datetime import date

from bancoDados.src.conexion.oracle_queries import OracleQueries
from bancoDados.src.controller.controller_cliente import ControllerCliente
from bancoDados.src.controller.controller_tecnicos import ControllerTecnico
from bancoDados.src.model.clientes import Cliente
from bancoDados.src.model.ordens_servico import OrdemServico
from bancoDados.src.model.tecnicos import Tecnico


class ControllerOrdemServico:
    def __init__(self):
        self.ctrl_cliente = ControllerCliente()
        self.ctrl_tecnico = ControllerTecnico()

    def inserir_ordem_servico(self) -> OrdemServico:

        oracle = OracleQueries()

        self.listar_clientes(oracle, need_connect=True)
        cliente_id = int(input("Digite o ID do cliente: "))
        cliente = self.valida_cliente(oracle, cliente_id)
        if cliente==None:
            return None

        self.listar_tecnicos(oracle, need_connect=True)
        tecnico_id = int(input("Digite o ID do técnico: "))
        tecnico = self.valida_tecnico(oracle, tecnico_id)
        if tecnico==None:
            return None

        data_abertura = date(input("Informe a data de abertura da Ordem de Serviço (DD/MM/AAAA): "))
        data_conclusao = date(input("Informe a data de conclusão da Ordem de Serviço (DD/MM/AAAA): "))
        status = str(input("Informe o status da Ordem de Serviço: "))
        solucao = str(input("Informe a solução da ordem de serviço: "))
        custo_total = float(input("Informe o custo total da ordem de serviço: "))

        cursor = oracle.connect()

        output_value = cursor.var(int)

        data = dict(codigo=output_value, cliente_id=int(cliente.get_cliente_id()),
                    tecnico_id=int(tecnico.get_tecnico_id()), data_abertura=data_abertura,
                    data_conclusao=data_conclusao, status=status,  solucao=solucao, custo_total=custo_total)

        cursor.execute("""
                        begin
                            :codigo := ORDEM_SERVICO_ORDEM_ID_SEQ.NEXTVAL:
                            insert into ordens_servico values(:codigo, :data_abertura, :data_conclusao, :status, 
                                                              :solucao, :custo_total);
                        end    
                        """, data)

        ordem_id = output_value.getvalue()
        oracle.conn.commit()

        df_ordem_servico = oracle.sqlToDataFrame(f"select ordem_id, data_abertura, data_conclusao, status, solucao, "
                                                 f"custo_total from ordens_servico where ordem_id = {ordem_id}")

        nova_ordem_servico = OrdemServico(df_ordem_servico.ordem_id.values[0], cliente, tecnico,
                                          df_ordem_servico.data_abertura.values[0],
                                          df_ordem_servico.data_conclusao.values[0], df_ordem_servico.status.values[0],
                                          df_ordem_servico.solucao.values[0], df_ordem_servico.custo_total.values[0])

        print(nova_ordem_servico.to_string())
        return nova_ordem_servico

    def atualizar_ordem_servico(self) -> OrdemServico:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        ordem_id = int(input("Informe o número da ordem de serviço que será alterada: "))

        if not self.verifica_existencia_ordem_servico(oracle, ordem_id):

            self.listar_clientes(oracle, need_connect=True)
            cliente_id = int(input("Digite o ID do cliente: "))
            cliente = self.valida_cliente(oracle, cliente_id)
            if cliente == None:
                return None

            self.listar_tecnicos(oracle, need_connect=True)
            tecnico_id = int(input("Digite o ID do técnico: "))
            tecnico = self.valida_tecnico(oracle, tecnico_id)
            if tecnico == None:
                return None

            data_abertura = date(input("Informe a nova data de abertura da Ordem de Serviço (DD/MM/AAAA): "))
            data_conclusao = date(input("Informe a nova data de conclusão da Ordem de Serviço (DD/MM/AAAA): "))
            status = str(input("Informe o status novo da Ordem de Serviço: "))
            solucao = str(input("Informe a solução nova da ordem de serviço: "))
            custo_total = float(input("Informe o custo total da ordem de serviço: "))

            oracle.write(f"update ordens_servico set cliente_id = {cliente.get_cliente_id()}, "
                         f"tecnico_id = {tecnico.get_tecnico_id()}, data_abertura = {data_abertura}, "
                         f"data_conclusa = {data_conclusao}, status = {status}, solucao = {solucao}, "
                         f"custo_total = {custo_total} where ordem_id = {ordem_id}")

            df_ordem_servico = oracle.sqlToDataFrame(f"select ordem_id, data_abertura, data_conclusao, status, solucao,"
                                                     f"custo_total from ordens_servico where ordem_id = {ordem_id}")

            ordem_servico_atualizada = OrdemServico(df_ordem_servico.ordem_id.values[0], cliente, tecnico,
                                            df_ordem_servico.data_abertura.values[0],
                                            df_ordem_servico.data_conclusao.values[0], df_ordem_servico.status.values[0],
                                            df_ordem_servico.solucao.values[0], df_ordem_servico.custo_total.values[0])

            print(ordem_servico_atualizada.to_string())
            return ordem_servico_atualizada
        else:
            print(f"A ordem de serviço nº, {ordem_id}, não existe. ")

    def excluir_ordem_servico(self) -> OrdemServico:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        ordem_id = int(input("Informe o número da ordem de serviço que será excluída: "))

        if not self.verifica_existencia_ordem_servico(oracle, ordem_id):

            df_ordem_servico = oracle.sqlToDataFrame(f"select ordem_id, data_abertura, data_conclusao, status, solucao,"
                                                     f"custo_total from ordens_servico "f"where ordem_id = {ordem_id}")

            cliente = self.valida_cliente(oracle, df_ordem_servico.cliente_id.values[0])
            tecnico = self.valida_tecnico(oracle, df_ordem_servico.tecnico_id.values[0])

            opcao_excluir = input(f"Tem certeza que deseja excluir a ordem de serviço nº {ordem_id} (S|N)? ")

            if opcao_excluir.lower() == "S":

                oracle.write(f"delete from ordens_servico where ordem_id = {ordem_id}")

                ordem_servico_excluida = OrdemServico(df_ordem_servico.ordem_id.values[0], cliente, tecnico,
                                                      df_ordem_servico.data_abertura.values[0],
                                                      df_ordem_servico.data_conclusao.values[0],
                                                      df_ordem_servico.status.values[0],
                                                      df_ordem_servico.solucao.values[0],
                                                      df_ordem_servico.custo_total.values[0])

            print("Ordem de serviço excluída com sucesso!")
            return ordem_servico_excluida

        else:
            print(f"A ordem de serviço nº, {ordem_id}, não existe. ")


    def verifica_existencia_ordem_servico(self, oracle: OracleQueries, ordem_id: int = None)-> bool:
        df_ordem_servico = oracle.sqlToDataFrame(f"select ordem_id, cliente_id, tecnico_id, data_abertura, "
                                                 f"data_conclusao, status, solucao, custo_total from ordens_servico "
                                                 f"where ordem_id = {ordem_id}")
        return df_ordem_servico.empty

    def listar_clientes(self, oracle: OracleQueries, need_connect: bool = False):
        query = """
                select c.cliente_id_cliente
                    , c.nome_cliente
                    , c.endereco_cliente
                    , c.email_cliente
                    , c.telefone_cliente
                    
                from clientes c
                order by c.cliente_id_cliente
                """

        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_tecnicos(self, oracle: OracleQueries, need_connect: bool = False):
        query = """
                select t.tecnico_id_tecnico
                    , t.nome_tecnico
                    , t.endereco_tecnico
                    , t.email_tecnico
                    , t.telefone_tecnico

                from tecnicos t
                order by t.tecnico_id_tecnico
                """

        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_cliente(self, oracle: OracleQueries, cliente_id_cliente: int = None) -> Cliente:
        if self.ctrl_cliente.verifica_existencia_cliente(oracle, cliente_id_cliente):
            print(f"O ID do cliente informado, {cliente_id_cliente}, não existe na base.")
            return None
        else:
            oracle.connect()

            df_cliente = oracle.sqlToDataFrame(f"select cliente_id_cliente, nome_cliente, endereco_cliente, "
                                               f"email_cliente, telefone_cliente from clientes "
                                               f"where cliente_id_cliente = '{cliente_id_cliente}'")

            cliente = Cliente(df_cliente.cliente_id_cliente.values[0], df_cliente.nome_cliente.values[0],
                              df_cliente.endereco_cliente.values[0], df_cliente.email_cliente.values[0],
                              df_cliente.telefone_cliente.values[0])
            return cliente

    def valida_tecnico(self, oracle: OracleQueries, tecnico_id_tecnico: int = None) -> Tecnico:
        if self.ctrl_tecnico.verifica_existencia_tecnico(oracle, tecnico_id_tecnico):
            print(f"O ID do tecnico informado, {tecnico_id_tecnico}, não existe na base.")
            return None
        else:
            oracle.connect()

            df_tecnico = oracle.sqlToDataFrame(f"select tecnico_id_tecnico, nome_tecnico, especialidade_tecnico, "
                                               f"email_tecnico, telefone_tecnico from tecnicos where "
                                               f"tecnico_id_tecnico = '{tecnico_id_tecnico}'")

            tecnico = Tecnico(df_tecnico.tecnico_id_tecnico.values[0], df_tecnico.nome_tecnico.values[0],
                              df_tecnico.especialidade_tecnico.values[0], df_tecnico.email_tecnico.values[0],
                              df_tecnico.telefone_tecnico.values[0])
            return tecnico
