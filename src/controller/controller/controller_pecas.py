from bancoDados.src.conexion.oracle_queries import OracleQueries
from bancoDados.src.model.pecas import Peca


class ControllerPeca:
    def __init__(self):
        pass

    def inserir_peca(self) -> Peca:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        peca_id = int(input("Informe o ID da peça que será cadastrada: "))

        if self.verifica_existencia_peca(oracle, peca_id):
            nome = input("Nome da peça: ")
            preco_uni = input("Preço unitário: ")

            oracle.write(f"insert into pecas values('{peca_id}', '{nome}', '{preco_uni}')")

            df_peca = oracle.sqlToDataFrame(f"select peca_id, nome, preco_uni from pecas where peca_id = '{peca_id}'")

            nova_peca = Peca(df_peca.peca_id.values[0], df_peca.nome.values[0], df_peca.preco_uni.values[0])

            print(nova_peca.to_String())

            return nova_peca
        else:
            print(f"O ID {peca_id} já foi cadastrado em sistema.")
            return None

    def atualizar_peca(self) -> Peca:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        peca_id = int(input("Informe o ID da peça que será atualizada: "))

        if not self.verifica_existencia_peca(oracle, peca_id):
            novo_nome = input("Novo nome da peça: ")
            novo_preco_uni = input("Novo preço unitário: ")

            oracle.write(f"update into pecas set nome = '{novo_nome}', preco_uni = '{novo_preco_uni}' where peca_id '{peca_id}')")

            df_peca = oracle.sqlToDataFrame(f"select peca_id, nome, preco_uni from pecas where peca_id = '{peca_id}'")

            peca_alterada = Peca(df_peca.peca_id.values[0], df_peca.nome.values[0], df_peca.preco_uni.values[0])

            print(peca_alterada.to_String())

            return peca_alterada
        else:
            print(f"O ID {peca_id} não está cadastrado em sistema.")
            return None

    def excluir_peca(self) -> Peca:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        peca_id = int(input("Informe o ID da peça que será excluída: "))

        if not self.verifica_existencia_peca(oracle, peca_id):
            df_peca = oracle.sqlToDataFrame(f"select peca_id, nome, preco_uni from pecas where peca_id = '{peca_id}'")

            oracle.write(f"delete from pecas where peca_id = {peca_id}")

            peca_excluida = Peca(df_peca.peca_id.values[0], df_peca.nome.values[0], df_peca.preco_uni.values[0])

            print("Peça excluída com sucesso!")
            print(peca_excluida.to_String())

        else:
            print(f"O ID {peca_id} não está cadastrado em sistema.")

    def verifica_existencia_peca(self, oracle: OracleQueries, peca_id: int = None) -> bool:
        df_peca = oracle.sqlToDataFrame(f"select peca_id, nome, preco_uni from pecas where peca_id = '{peca_id}'")
        return df_peca.empty