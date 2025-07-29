import tkinter as tk
from tkinter import PhotoImage

# Criar janela principal
root = tk.Tk()
root.title("K&M Storage")
root.geometry("900x500")
root.configure(bg="#38b6ff")

# Logo (coloque o caminho real da imagem .png abaixo)
try:
    logo = PhotoImage(file="logo.png")
    tk.Label(root, image=logo, bg="#38b6ff").place(x=380, y=10)
except:
    tk.Label(root, text="K&M STORAGE", font=("Arial", 24, "bold"), bg="#38b6ff", fg="white").place(x=350, y=20)

# Texto lateral
texto = (
    "Você está a um passo de\n"
    "acessar o melhor aplicativo\n"
    "de controle de estocagem!\n"
    "Basta cadastrar-se"
)
tk.Label(root, text=texto, font=("Arial", 16, "bold"),
         bg="#38b6ff", fg="white", justify="left").place(x=30, y=140)

# Frame de cadastro
frame = tk.Frame(root, bg="white", bd=0, relief="flat")
frame.place(x=350, y=130)

tk.Label(frame, text="CADASTRO", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=(10, 20))

# Campo Nome
entry_nome = tk.Entry(frame, width=35, font=("Arial", 12))
entry_nome.insert(0, "Digite seu nome:")
entry_nome.pack(pady=5)

# Campo Email
entry_email = tk.Entry(frame, width=35, font=("Arial", 12))
entry_email.insert(0, "Digite um E-Mail:")
entry_email.pack(pady=5)

# Campo Senha
entry_senha = tk.Entry(frame, width=35, font=("Arial", 12), show="*")
entry_senha.insert(0, "Crie uma senha:")
entry_senha.pack(pady=5)

# Botão Cadastrar
btn_cadastrar = tk.Button(frame, text="CADASTRAR", bg="#1b4f72", fg="white",
                          font=("Arial", 12, "bold"), width=25)
btn_cadastrar.pack(pady=(15, 10))

# Imagem do pato (coloque o caminho real da imagem .png abaixo)
try:
    pato = PhotoImage(file="pato.png")
    tk.Label(root, image=pato, bg="#38b6ff").place(x=700, y=280)
except:
    tk.Label(root, text="[imagem do pato aqui]", bg="#38b6ff", fg="white").place(x=700, y=280)

# Iniciar aplicação
root.mainloop()
