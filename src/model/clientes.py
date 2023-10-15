class Cliente:
    def __init__(self,
                cliente_id: int = None,
                nome: str = None,
                endereco: str = None,
                email: str = None,
                telefone: str = None):
        self.set_cliente_id(cliente_id)
        self.set_nome(nome)
        self.set_endereco(endereco)
        self.set_email(email)
        self.set_telefone(telefone)

    def set_cliente_id(self, cliente_id: int):
        self.cliente_id = cliente_id

    def set_nome(self, nome: str):
        self.nome = nome

    def set_endereco(self, endereco: str):
        self.endereco = endereco

    def set_email(self, email: str):
        self.email = email

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def get_cliente_id(self) -> int:
        return self.cliente_id

    def get_nome(self) -> str:
        return self.nome

    def get_endereco(self) -> str:
        return self.endereco

    def get_email(self) -> str:
        return self.email

    def get_telefone(self) -> str:
        return self.telefone

    def to_String(self) -> str:
        return f"Cliente ID: {self.cliente_id()} | Nome: {self.nome()} | Endereço: {self.endereco()} " \
               f"| Email: {self.email} | Telefone: {self.telefone}"
