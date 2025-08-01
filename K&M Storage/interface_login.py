import tkinter as tk
from tkinter import messagebox, PhotoImage
from database import conectar_banco
import subprocess  # Para abrir outro script Python

def limpar_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black", show="*" if "senha" in placeholder.lower() else "")

def criar_entry(master, placeholder, show=None):
    entry = tk.Entry(master, width=35, font=("Arial", 12), fg="gray", show=show)
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: limpar_placeholder(event, entry, placeholder))
    entry.pack(pady=8)
    return entry

def realizar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if not email or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            messagebox.showinfo("Login realizado", f"Bem-vindo, {usuario[1]}!")
            janela.destroy()  # Fecha a janela atual
            subprocess.Popen(["python", "pagina_principal.py"])  # Abre a próxima tela
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos. Tente novamente!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar com o banco: {str(e)}")

# Janela principal
janela = tk.Tk()
janela.title("K&M Storage")
janela.geometry("1080x600")
janela.resizable(False, False)
janela.configure(bg="#38b6ff")

try:
    janela.iconphoto(False, PhotoImage(file="icon.png"))
except:
    pass  # Evita erro se ícone não for encontrado
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

# Imagem do pato
try:
    pato = PhotoImage(file="pato.png")
    tk.Label(janela, image=pato, bg="#38b6ff").place(x=750, y=200)
except:
    tk.Label(janela, text="[imagem do pato aqui]", bg="#38b6ff", fg="white").place(x=700, y=280)

janela.mainloop()
