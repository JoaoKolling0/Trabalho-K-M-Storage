import tkinter as tk
from tkinter import ttk
from database import listar_mercadorias

class VerMercadorias:
    def __init__(self, master, email_usuario):
        self.master = master
        self.email = email_usuario
        self.janela = tk.Toplevel(master)
        self.janela.title("Mercadorias em Estoque")
        self.janela.geometry("800x600")
        self.janela.resizable(True, True)
        self.janela.configure(bg="#f0f0f0")

        self.criar_widgets()
        self.carregar_dados()

    def criar_widgets(self):
        tk.Label(self.janela, text="Suas Mercadorias em Estoque", 
                font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Treeview para mostrar as mercadorias
        self.tree = ttk.Treeview(self.janela, columns=("Nome", "Quantidade", "Entrada", "Rastreio"), show="headings")
        
        # Configuração das colunas
        self.tree.heading("Nome", text="Nome da Mercadoria")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Entrada", text="Data de Entrada")
        self.tree.heading("Rastreio", text="Código de Rastreio")
        
        self.tree.column("Nome", width=200)
        self.tree.column("Quantidade", width=100, anchor="center")
        self.tree.column("Entrada", width=150, anchor="center")
        self.tree.column("Rastreio", width=200, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.janela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

    def carregar_dados(self):
        mercadorias = listar_mercadorias(self.email)
        for mercadoria in mercadorias:
            self.tree.insert("", "end", values=mercadoria)