class Tecnico:
    def __init__(self,
                tecnico_id: int = None,
                nome: str = None,
                especialidade: str = None,
                email: str = None,
                telefone: str = None):
        self.set_tecnico_id(tecnico_id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_email(email)
        self.set_telefone(telefone)

    def set_tecnico_id(self, tecnico_id: int):
        self.tecnico_id = tecnico_id

    def set_nome(self, nome: str):
        self.nome = nome

    def set_especialidade(self, especialidade: str):
        self.especialidade = especialidade

    def set_email(self, email: str):
        self.email = email

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def get_tecnico_id(self) -> int:
        return self.tecnico_id

    def get_nome(self) -> str:
        return self.nome

    def get_especialidade(self) -> str:
        return self.especialidade

    def get_email(self) -> str:
        return self.email

    def get_telefone(self) -> str:
        return self.telefone

    def to_String(self) -> str:
        return f"Tecnico ID: {self.tecnico_id()} | Nome: {self.nome()} | Especialidade: {self.especialidade()} " \
               f"| Email: {self.email} | Telefone: {self.telefone}"
