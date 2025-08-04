import tkinter as tk
from tkinter import messagebox, ttk
from database import buscar_por_rastreio

class RastrearMercadoria:
    def __init__(self, master, email_usuario):
        self.master = master
        self.email = email_usuario
        self.janela = tk.Toplevel(master)
        self.janela.title("Rastrear Mercadoria")
        self.janela.geometry("600x400")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#f0f0f0")

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.janela, text="Rastrear Mercadoria pelos Correios", 
                font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Frame de entrada
        frame_entrada = tk.Frame(self.janela, bg="#f0f0f0")
        frame_entrada.pack(pady=20)

        tk.Label(frame_entrada, text="Código de Rastreio:", bg="#f0f0f0").grid(row=0, column=0, padx=5)
        self.entry_codigo = tk.Entry(frame_entrada, width=30, font=("Arial", 12))
        self.entry_codigo.grid(row=0, column=1, padx=5)

        tk.Button(frame_entrada, text="Buscar", bg="#2196F3", fg="white",
                 command=self.buscar).grid(row=0, column=2, padx=10)

        # Frame de resultados
        frame_resultados = tk.Frame(self.janela, bg="#f0f0f0")
        frame_resultados.pack(pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(frame_resultados, columns=("Nome", "Quantidade", "Entrada"), show="headings")
        self.tree.heading("Nome", text="Nome da Mercadoria")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Entrada", text="Data de Entrada")
        
        self.tree.column("Nome", width=200)
        self.tree.column("Quantidade", width=100, anchor="center")
        self.tree.column("Entrada", width=150, anchor="center")
        
        self.tree.pack(fill="both", expand=True)

    def buscar(self):
        codigo = self.entry_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Atenção", "Informe o código de rastreio!")
            return

        # Limpa resultados anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Busca no banco de dados
        resultados = buscar_por_rastreio(self.email, codigo)
        
        if not resultados:
            messagebox.showinfo("Resultado", "Nenhuma mercadoria encontrada com este código de rastreio.")
            return

        for mercadoria in resultados:
            self.tree.insert("", "end", values=mercadoria)