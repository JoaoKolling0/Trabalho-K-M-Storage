import tkinter as tk
from tkinter import messagebox
from database import adicionar_mercadoria
from datetime import datetime

class EnviarMercadoria:
    def __init__(self, master, email_usuario):
        self.master = master
        self.email = email_usuario
        self.janela = tk.Toplevel(master)
        self.janela.title("Enviar Mercadoria")
        self.janela.geometry("500x400")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#f0f0f0")

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.janela, text="Enviar Mercadoria para Estoque", 
                font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Frame principal
        frame = tk.Frame(self.janela, bg="#f0f0f0")
        frame.pack(pady=20)

        # Nome da mercadoria
        tk.Label(frame, text="Nome da Mercadoria:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nome = tk.Entry(frame, width=30, font=("Arial", 12))
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        # Quantidade
        tk.Label(frame, text="Quantidade:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_quantidade = tk.Entry(frame, width=30, font=("Arial", 12))
        self.entry_quantidade.grid(row=1, column=1, padx=10, pady=5)

        # Código de rastreio (opcional)
        tk.Label(frame, text="Código de Rastreio (opcional):", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_rastreio = tk.Entry(frame, width=30, font=("Arial", 12))
        self.entry_rastreio.grid(row=2, column=1, padx=10, pady=5)

        # Botão de envio
        tk.Button(self.janela, text="Enviar para Estoque", bg="#4CAF50", fg="white",
                 font=("Arial", 12), command=self.enviar).pack(pady=20)

    def enviar(self):
        nome = self.entry_nome.get()
        quantidade = self.entry_quantidade.get()
        rastreio = self.entry_rastreio.get() or None

        if not nome or not quantidade:
            messagebox.showwarning("Atenção", "Preencha pelo menos nome e quantidade!")
            return

        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo!")
            return

        adicionar_mercadoria(self.email, nome, quantidade, rastreio)
        messagebox.showinfo("Sucesso", "Mercadoria enviada para o estoque com sucesso!")
        self.janela.destroy()