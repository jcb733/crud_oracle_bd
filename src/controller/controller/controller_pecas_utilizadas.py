from bancoDados.src.conexion.oracle_queries import OracleQueries
from bancoDados.src.controller.controller_ordens_servico import ControllerOrdemServico
from bancoDados.src.controller.controller_pecas import ControllerPeca
from bancoDados.src.model.ordens_servico import OrdemServico
from bancoDados.src.model.pecas import Peca
from bancoDados.src.model.pecas_utilizadas import PecaUtilizada


class ControllerPecaUtilizada:

    def __init__(self):
        self.ctrl_peca = ControllerPeca()
        self.ctrl_ordem_servico = ControllerOrdemServico()

    def inserir_peca_utilizada(self) -> PecaUtilizada:

        oracle = OracleQueries()

        self.listar_ordens_servico(oracle, need_connect=True)
        ordem_id = int(input("Informe o nº da ordem de serviço que deseja buscar: "))
        ordem_servico = self.valida_ordem_servico(oracle, ordem_id)
        if ordem_servico == None:
            return None

        self.listar_pecas(oracle, need_connect=True)
        peca_id = int(input("Digite o ID da peca: "))
        peca = self.valida_peca(oracle, peca_id)
        if peca==None:
            return None

        preco_uni = float(input("Informe o preço da peça: "))
        quant_utilizada = int(input("Informe a quantidade de peças utilizadas: "))

        cursor = oracle.connect()

        output_value = cursor.var(int)

        data = dict(codigo=output_value, peca_id=int(peca.get_peca_id()), ordem_id=int(ordem_servico.get_ordem_id()),
                    preco_uni=preco_uni, quant_utilizada=quant_utilizada)

        cursor.execute("""
                        begin
                            :codigo := PECAS_UTILIZADAS_PECA_UTILIZADA_ID_SEQ.NEXTVAL:
                            insert into pecas_utilizadas values(:codigo, :preco_uni, :quant_utilizada)
                        end
                        """, data)

        codigo = output_value.getvalue()
        oracle.conn.commit()

        df_peca_utilizada = oracle.sqlToDataFrame(f"select peca_utilizada_id, preco_uni, quant_utilizada from "
                                                      f"pecas_utilizadas where peca_utilizada_id = {codigo}")

        nova_peca_utilizada = PecaUtilizada(df_peca_utilizada.codigo.values[0], peca, ordem_servico,
                                            df_peca_utilizada.preco_uni.values[0],
                                            df_peca_utilizada.quant_utilizada.values[0])
        print(nova_peca_utilizada.to_String())
        return nova_peca_utilizada

    def atualizar_peca_utilizada(self) -> PecaUtilizada:
        oracle = OracleQueries(can_write=True)

        codigo = int(input("Informe o código da peça utilizada que será alterada: "))

        if not self.verifica_existencia_peca_utilizada(oracle, codigo):

            self.listar_ordens_servico(oracle, need_connect=True)
            ordem_id = int(input("Informe o nº da ordem de serviço que deseja buscar: "))
            ordem_servico = self.valida_ordem_servico(oracle, ordem_id)
            if ordem_servico == None:
                return None

            self.listar_pecas(oracle, need_connect=True)
            peca_id = int(input("Digite o ID da peca: "))
            peca = self.valida_peca(oracle, peca_id)
            if peca == None:
                return None

            preco_uni = float(input("Informe o novo preço da peça: "))
            quant_utilizada = int(input("Informe a nova quantidade de peças utilizadas: "))

            oracle.write(f"update pecas_utilizadas set peca_utilizada_id = {codigo}, peca_id = {peca.get_peca_id()},"
                         f"ordem_id = {ordem_servico.get_ordem_id()}, preco_uni = {preco_uni}, "
                         f"quant_utilizada = {quant_utilizada} where peca_utilizada_id = {codigo}")

            df_peca_utilizada = oracle.sqlToDataFrame(f"select peca_utilizada_id, preco_uni, quant_utilizada from "
                                                      f"pecas_utilizadas where peca_utilizada_id = {codigo}")

            peca_utilizada_atualizada = PecaUtilizada(df_peca_utilizada.codigo.values[0], peca, ordem_servico,
                                                      df_peca_utilizada.preco_uni.values[0],
                                                      df_peca_utilizada.quant_utilizada.values[0])
            print(peca_utilizada_atualizada.to_String())
            return peca_utilizada_atualizada
        else:
            print(f"O código da peça utilizada, {codigo}, não existe")

    def excluir_peca_utilizada(self) -> PecaUtilizada:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo = int(input("Informe o código da peça utilizada que será alterada: "))

        if not self.verifica_existencia_peca_utilizada(oracle, codigo):

            df_peca_utilizada = oracle.sqlToDataFrame(f"select peca_utilizada_id, preco_uni, quant_utilizada from "
                                                      f"pecas_utilizadas where peca_utilizada_id = {codigo}")

            peca = self.valida_peca(oracle, df_peca_utilizada.peca_id.values[0])
            ordem_servico = self.valida_ordem_servico(oracle, df_peca_utilizada.ordem_id.values[0])

            opcao_excluir = input(f"Tem certeza que deseja excluir a peça utilizada código {codigo} (S|N)? ")

            if opcao_excluir.lower() == "S":

                oracle.write(f"delete from pecas_utilizadas where peca_utilizada_id = {codigo}")

                peca_utilizada_excluida = PecaUtilizada(df_peca_utilizada.codigo.values[0], peca, ordem_servico,
                                                        df_peca_utilizada.preco_uni.values[0],
                                                        df_peca_utilizada.quant_utilizada.values[0])
            print(peca_utilizada_excluida.to_String())
            return peca_utilizada_excluida
        else:
            print(f"O código da peça utilizada, {codigo}, não existe")


    def verifica_existencia_peca_utilizada(self, oracle: OracleQueries, codigo: int = None) -> bool:
        df_peca_utilizada = oracle.sqlToDataFrame(f"select peca_utilizada_id, preco_uni, quant_utilizada from "
                                                  f"pecas_utilizadas where peca_utilizada_id = {codigo}")
        return df_peca_utilizada

    def listar_pecas(self, oracle: OracleQueries, need_connect: bool = False):
        query = """
                select p.peca_id
                    , p.nome
                    , p.preco_uni
                from pecas p
                order by p.peca_id
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def listar_ordens_servico(self, oracle: OracleQueries, need_connect: bool = False):
        query = """
                select o.ordem_id
                    , c.cliente_id as cliente
                    , t.tecnico as tecnico
                    , o.data_abertura
                    , o.data_conclusao
                    , o.status
                    , o.solucao
                    , o.custo_total
                from ordens_servico o
                inner join clientes c
                on o.nome_cliente = c.nome
                inner join clientes c
                on o.endereco = c.endereco
                inner join tecnicos t
                on o.nome_tecnico = t.nome
                order by o.ordem_id
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_peca(self, oracle: OracleQueries, peca_id: int = None) -> Peca:
        if self.ctrl_peca.verifica_existencia_peca(oracle, peca_id):
            print(f"A peça, ID {peca_id}, não existe na base.")
            return None
        else:
            oracle.connect()

            df_peca = oracle.sqlToDataFrame(f"select peca_id, nome, preco_uni from pecas where peca_id = '{peca_id}")

            peca = Peca(df_peca.peca_id.values[0], df_peca.nome.values[0], df_peca.preco_uni.values[0])

            return peca

    def valida_ordem_servico(self, oracle: OracleQueries, ordem_id: int = None) -> OrdemServico:
        if self.ctrl_ordem_servico.verifica_existencia_ordem_servico(oracle, ordem_id):
            print(f"A ordem de serviço nº {ordem_id}, não foi encontrada na base.")
            return None
        else:
            oracle.connect()

            df_ordem_servico = oracle.sqlToDataFrame(f"select ordem_id, cliente_id, tecnico_id, data_abertura, "
                                                     f"data_conclusao, status, solucao, custo_total from ordens_servico"
                                                     f"where ordem_id = {ordem_id}")
            cliente = self.ctrl_ordem_servico.valida_cliente(oracle, df_ordem_servico.cliente_id.values[0])
            tecnico = self.ctrl_ordem_servico.valida_tecnico(oracle, df_ordem_servico.tecnico_id.values[0])

            ordem_servico = OrdemServico(df_ordem_servico.ordem_id.values[0], cliente, tecnico,
                                         df_ordem_servico.data_abertura.values[0],
                                         df_ordem_servico.data_conclusao.values[0], df_ordem_servico.status.values[0],
                                         df_ordem_servico.solucao.values[0], df_ordem_servico.custo_total.values[0])
            return ordem_servico
