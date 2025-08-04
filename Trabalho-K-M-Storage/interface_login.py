import tkinter as tk
from tkinter import messagebox, PhotoImage
from database import conectar_banco
import subprocess
import sys
from pagina_principal import abrir_pagina_principal

def limpar_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black", show="*" if "senha" in placeholder.lower() else "")

def restaurar_placeholder(event, entry, placeholder):
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(fg="gray", show="" if "senha" in placeholder.lower() else "")

def criar_entry(master, placeholder, show=None):
    entry = tk.Entry(master, width=35, font=("Arial", 12), fg="gray", show=show)
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: limpar_placeholder(event, entry, placeholder))
    entry.bind("<FocusOut>", lambda event: restaurar_placeholder(event, entry, placeholder))
    entry.pack(pady=8)
    return entry

def realizar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if email == "Digite seu E-Mail:" or senha == "Digite sua senha:":
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            messagebox.showinfo("Login realizado", f"Bem-vindo, {usuario[0]}!")
            janela.destroy()
            abrir_pagina_principal(email)
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos. Tente novamente!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar com o banco: {str(e)}")

def voltar_para_inicio():
    janela.destroy()
    subprocess.Popen([sys.executable, "app.py"])

# Janela principal
janela = tk.Tk()
janela.title("K&M Storage")
janela.geometry("1080x600")
janela.resizable(False, False)
janela.configure(bg="#38b6ff")

try:
    janela.iconphoto(False, PhotoImage(file="icon.png"))
except:
    pass

# Logo
try:
    logo = PhotoImage(file="logo.png")
    tk.Label(janela, image=logo, bg="#38b6ff").place(x=446, y=6)
except:
    tk.Label(janela, text="K&M STORAGE", font=("Arial", 24, "bold"), bg="#38b6ff", fg="white").pack(pady=10)

# Texto lateral
texto = (
    "\n\n\n\nQue bom te ver de novo\n"
    "por aqui!"
)
tk.Label(janela, text=texto, font=("Arial", 16, "bold"),
         bg="#38b6ff", fg="white", justify="left").place(x=30, y=140)

# Caixa de login
frame = tk.Frame(janela, bg="white", padx=25, pady=20)
frame.place(x=330, y=200)

tk.Label(frame, text="Login", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=(0, 10))

# Campos de login
entry_email = criar_entry(frame, "Digite seu E-Mail:")
entry_senha = criar_entry(frame, "Digite sua senha:")

# Botão de login
tk.Button(frame, text="LOGAR", bg="#1b4f72", fg="white",
          font=("Arial", 12, "bold"), width=30, command=realizar_login).pack(pady=(15, 5))

# Botão Voltar
tk.Button(janela, text="Voltar", bg="#7f8c8d", fg="white",
          font=("Arial", 10), command=voltar_para_inicio).place(x=10, y=550)

# Imagem do pato
try:
    pato = PhotoImage(file="pato.png")
    tk.Label(janela, image=pato, bg="#38b6ff").place(x=750, y=200)
except:
    tk.Label(janela, text="[imagem do pato aqui]", bg="#38b6ff", fg="white").place(x=700, y=280)

janela.mainloop()