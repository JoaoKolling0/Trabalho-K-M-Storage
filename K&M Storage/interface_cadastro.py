import tkinter as tk
from tkinter import PhotoImage

def limpar_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def criar_entry(master, placeholder):
    entry = tk.Entry(master, width=35, font=("Arial", 12), fg="gray")
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: limpar_placeholder(event, entry, placeholder))
    entry.pack(pady=8)
    return entry

# Janela principal
root = tk.Tk()
root.title("K&M Storage")
root.geometry("1080x600")
root.configure(bg="#38b6ff")

# Logo (ajuste o caminho da imagem se necessário)
try:
    logo = PhotoImage(file="icon.png")
    tk.Label(root, image=logo, bg="#38b6ff").place(x=446, y=6)
except:
    tk.Label(root, text="K&M STORAGE", font=("Arial", 24, "bold"), bg="#38b6ff", fg="white").pack(pady=10)

# Texto lateral
texto = (
    "\n\n\n\nVocê está a um passo de\n"
    "acessar o melhor aplicativo\n"
    "de controle de estocagem!\n"
    "Basta cadastrar-se"
)
tk.Label(root, text=texto, font=("Arial", 16, "bold"),
         bg="#38b6ff", fg="white", justify="left").place(x=30, y=140)

# Caixa de cadastro (frame branco)
frame = tk.Frame(root, bg="white", padx=25, pady=20)
frame.place(x=330, y=160)

tk.Label(frame, text="CADASTRO", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=(0, 10))

# Campos
entry_nome = criar_entry(frame, "Digite seu nome:")
entry_email = criar_entry(frame, "Digite um E-Mail:")
entry_senha = criar_entry(frame, "Digite uma senha:")
entry_confirma = criar_entry(frame, "Confirme sua senha:")


# Botão
tk.Button(frame, text="CADASTRAR", bg="#1b4f72", fg="white",
          font=("Arial", 12, "bold"), width=30).pack(pady=(15, 5))

# Imagem do pato (opcional)
try:
    pato = PhotoImage(file="pato.png")
    tk.Label(root, image=pato, bg="#38b6ff").place(x=750, y=200)
except:
    tk.Label(root, text="[imagem do pato aqui]", bg="#38b6ff", fg="white").place(x=700, y=280)

root.mainloop()
