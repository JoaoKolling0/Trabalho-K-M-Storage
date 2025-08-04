import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import subprocess
import sys

def abrir_login():
    janela.destroy()
    subprocess.Popen([sys.executable, "interface_login.py"])

def abrir_cadastro():
    janela.destroy()
    subprocess.Popen([sys.executable, "interface_cadastro.py"])

def iniciar_aplicacao():
    global janela
    # Criação da janela
    janela = tk.Tk()
    janela.title("K&M Storage")
    janela.geometry("1150x650")
    janela.resizable(False, False)
    janela.configure(bg="#38b6ff")

    # Ícone da janela
    try:
        janela.iconphoto(False, PhotoImage(file="icon.png"))
    except:
        pass  # Evita erro se ícone não for encontrado

    # Título superior
    titulo = tk.Label(
        janela, text="Seja Bem-vindo ao nosso APP, faça login ou seu cadastro",
        bg="#38b6ff", fg="white", font=("Arial", 15, "bold")
    )
    titulo.pack(pady=10)

    # Imagem central da logo
    try:
        logo_img = Image.open("logo.png").resize((180, 180))
        logo_tk = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(janela, image=logo_tk, bg="#38b6ff")
        logo_label.place(relx=0.5, rely=0.22, anchor="center")
    except:
        pass

    # Imagem da empilhadeira (à esquerda)
    try:
        img = Image.open("estoque.png")
        img_tk = ImageTk.PhotoImage(img)
        imagem_label = tk.Label(janela, image=img_tk, bg="#38b6ff")
        imagem_label.place(x=50, y=200)
    except:
        pass

    # Botão LOGIN
    botao_login = tk.Button(
        janela, text="LOGIN", command=abrir_login,
        bg="#1b4b5a", fg="white", font=("Arial", 14, "bold"),
        width=20, height=2
    )
    botao_login.place(relx=0.5, rely=0.48, anchor="center")

    # Texto "OU SE AINDA..."
    texto_ou = tk.Label(
        janela, text="OU SE AINDA NÃO\nTIVER UMA CONTA:",
        bg="#38b6ff", fg="white", font=("Arial", 10, "bold")
    )
    texto_ou.place(relx=0.5, rely=0.58, anchor="center")

    # Botão CADASTRAR-SE
    botao_cadastrar = tk.Button(
        janela, text="CADASTRAR-SE", command=abrir_cadastro,
        bg="#b91c1c", fg="white", font=("Arial", 14, "bold"),
        width=20, height=2
    )
    botao_cadastrar.place(relx=0.5, rely=0.68, anchor="center")

    # Caixa do lado direito (desenvolvedores)
    frame_desenvolvedores = tk.Frame(janela, bg="#f97316", width=250, height=150)
    frame_desenvolvedores.place(x=780, y=220)

    texto_desenvolvedores = tk.Label(
        frame_desenvolvedores,
        text="App desenvolvido por:\n\n- João Kolling\n- Rafael Rodrigues",
        bg="#f97316", fg="white", font=("Arial", 11, "bold"), justify="left"
    )
    texto_desenvolvedores.pack(padx=15, pady=15)

    # Rodapé
    rodape = tk.Label(
        janela,
        text="K&M Interprises 2025, todos os direitos reservados",
        bg="#38b6ff", fg="white", font=("Arial", 9)
    )
    rodape.pack(side="bottom", anchor="se", padx=10, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_aplicacao()