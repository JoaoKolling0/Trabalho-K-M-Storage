import tkinter as tk
from tkinter import messagebox, ttk
from database import retirar_mercadoria, listar_mercadorias

class RetirarMercadoria:
    def __init__(self, master, email_usuario):
        self.master = master
        self.email = email_usuario
        self.janela = tk.Toplevel(master)
        self.janela.title("Retirar Mercadoria")
        self.janela.geometry("600x500")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#f0f0f0")

        self.criar_widgets()
        self.atualizar_lista()

    def criar_widgets(self):
        tk.Label(self.janela, text="Retirar Mercadoria do Estoque", 
                font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Frame da lista
        frame_lista = tk.Frame(self.janela, bg="#f0f0f0")
        frame_lista.pack(pady=10)

        # Treeview para mostrar as mercadorias
        self.tree = ttk.Treeview(frame_lista, columns=("Nome", "Quantidade", "Entrada"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Entrada", text="Data de Entrada")
        self.tree.column("Nome", width=200)
        self.tree.column("Quantidade", width=100, anchor="center")
        self.tree.column("Entrada", width=150, anchor="center")
        self.tree.pack()

        # Frame de controles
        frame_controles = tk.Frame(self.janela, bg="#f0f0f0")
        frame_controles.pack(pady=20)

        tk.Label(frame_controles, text="Quantidade a Retirar:", bg="#f0f0f0").grid(row=0, column=0, padx=5)
        self.entry_quantidade = tk.Entry(frame_controles, width=10, font=("Arial", 12))
        self.entry_quantidade.grid(row=0, column=1, padx=5)

        tk.Button(frame_controles, text="Retirar", bg="#f44336", fg="white",
                 command=self.retirar).grid(row=0, column=2, padx=10)

    def atualizar_lista(self):
        # Limpa a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adiciona os itens do banco de dados
        mercadorias = listar_mercadorias(self.email)
        for mercadoria in mercadorias:
            self.tree.insert("", "end", values=(mercadoria[0], mercadoria[1], mercadoria[2]))

    def retirar(self):
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Atenção", "Selecione uma mercadoria!")
            return

        quantidade = self.entry_quantidade.get()
        if not quantidade:
            messagebox.showwarning("Atenção", "Informe a quantidade!")
            return

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo!")
            return

        nome_mercadoria = self.tree.item(item_selecionado)['values'][0]
        sucesso, mensagem = retirar_mercadoria(self.email, nome_mercadoria, quantidade)
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.atualizar_lista()
        else:
            messagebox.showerror("Erro", mensagem)