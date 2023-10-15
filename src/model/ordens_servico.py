from datetime import date
from bancoDados.src.model.clientes import Cliente
from bancoDados.src.model.tecnicos import Tecnico


class OrdemServico:
    def __init__(self,
                 ordem_id: int = None,
                 cliente_id: Cliente = None,
                 tecnico_id: Tecnico = None,
                 data_abertura: date = None,
                 data_conclusao: date = None,
                 status: str = None,
                 solucao: str = None,
                 custo_total: float = None):
        self.set_ordem_id(ordem_id)
        self.set_cliente_id(cliente_id)
        self.set_tecnico_id(tecnico_id)
        self.set_data_abertura(data_abertura)
        self.set_data_conclusao(data_conclusao)
        self.set_status(status)
        self.set_solucao(solucao)
        self.set_custo_total(custo_total)

    def set_ordem_id(self, ordem_id: int):
        self.ordem_id = ordem_id

    def set_cliente_id(self, cliente_id: Cliente):
        self.cliente_id = cliente_id

    def set_tecnico_id(self, tecnico_id: Tecnico):
        self.tecnico_id = tecnico_id

    def set_data_abertura(self, data_abertura: date):
        self.data_abertura = data_abertura

    def set_data_conclusao(self, data_conclusao: date):
        self.data_conclusao = data_conclusao

    def set_status(self, status: str):
        self.status = status

    def set_solucao(self, solucao: str):
        self.solucao = solucao

    def set_custo_total(self, custo_total: float):
        self.custo_total = custo_total

    def get_ordem_id(self) -> int:
        return self.ordem_id

    def get_cliente_id(self) -> Cliente:
        return self.cliente_id

    def get_tecnico_id(self) -> Tecnico:
        return self.tecnico_id

    def get_data_abertura(self) -> date:
        return self.data_abertura

    def get_data_conclusao(self) -> date:
        return self.data_conclusao

    def get_status(self) -> str:
        return self.status

    def get_solucao(self) -> str:
        return self.solucao

    def get_custo_total(self) -> float:
        return self.custo_total

    def to_string(self) -> str:
        return f"Ordem de Serviço ID: {self.ordem_id()} | Cliente ID: {self.cliente_id()} | Tecnico ID: {self.tecnico_id()} | " \
               f"Data de abertura: {self.data_abertura()}| Data de conclusão: {self.data_conclusao()} | Status: {self.status()} " \
               f"Solução: {self.solucao()} | Custo total: {self.custo_total()} "
