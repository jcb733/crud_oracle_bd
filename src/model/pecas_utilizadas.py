from bancoDados.src.model.ordens_servico import OrdemServico
from bancoDados.src.model.pecas import Peca

class PecaUtilizada:
    def __init__(self,
                 codigo: int = None,
                 peca_id: Peca = None,
                 ordem_id: OrdemServico = None,
                 preco_uni: float = None,
                 quant_utilizada: int = None):
        self.set_codigo(codigo)
        self.set_peca_id(peca_id)
        self.set_ordem_id(ordem_id)
        self.set_preco_uni(preco_uni)
        self.set_quant_utilizada(quant_utilizada)

    def set_codigo(self, codigo: int):
        self.codigo = codigo

    def set_peca_id(self, peca_id: Peca):
        self.peca_id = peca_id

    def set_ordem_id(self, ordem_id: OrdemServico):
        self.ordem_id = ordem_id

    def set_preco_uni(self, preco_uni: float):
        self.preco_uni = preco_uni

    def set_quant_utilizada(self, quant_utilizada: str):
        self.quant_utilizada = quant_utilizada

    def get_codigo(self) -> int:
        return self.codigo

    def get_peca_id(self) -> Peca:
        return self.peca_id

    def get_ordem_id(self) -> OrdemServico:
        return self.ordem_id

    def get_preco_uni(self) -> float:
        return self.preco_uni

    def get_quant_utilizada(self) -> int:
        return self.quant_utilizada

    def to_String(self) -> str:
        return f"Codigo: {self.codigo()} | Peca ID: {self.peca_id()} | Ordem de Serviço: {self.ordem_id()}" \
               f"| Preço Unitário: {self.preco_uni} | Quantidade Utilizada: {self.quant_utilizada}"
