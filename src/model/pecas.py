class Peca:
    def __init__(self,
                 peca_id: int = None,
                 nome: str = None,
                 preco_uni: float = None):
        self.set_peca_id(peca_id)
        self.set_nome(nome)
        self.set_preco_uni(preco_uni)

    def set_peca_id(self, peca_id: int):
        self.peca_id = peca_id

    def set_nome(self, nome: str):
        self.nome = nome

    def set_preco_uni(self, preco_uni: float):
        self.preco_uni = preco_uni

    def get_peca_id(self) -> int:
        return self.peca_id

    def get_nome(self) -> str:
        return self.nome

    def get_preco_uni(self) -> float:
        return self.preco_uni

    def to_String(self) -> str:
        return f"Peça ID: {self.peca_id()} | Nome: {self.nome()} | Preço Unitário: {self.preco_uni()} "
