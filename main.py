class User:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status
        
    def cadastro(self, email, senha):
        if self.status == "cadastrado":
            return f"{self.nome} já é cadastrado"
        
    def login(self, email, senha):
        self.email = email
        self.senha = senha
        