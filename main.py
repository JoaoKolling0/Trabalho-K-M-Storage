class User:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status
        
    def cadastro(self, cadastrar_email, cadastrar_senha):
        if self.status == "cadastrado":
            return f"{self.nome} já é cadastrado"
        else:
            self.cadastrar_email = cadastrar_email
            self.cadastrar_senha = cadastrar_senha
        
    def login(self, email, senha):
        self.email = email
        self.senha = senha
        