import tkinter as tk
from tkinter import PhotoImage, messagebox
from database import conectar_banco
from enviar_mercadoria import EnviarMercadoria
from retirar_mercadoria import RetirarMercadoria
from ver_mercadorias import VerMercadorias
from rastrear_mercadoria import RastrearMercadoria

def abrir_pagina_principal(email_usuario):
    janela = tk.Tk()
    janela.title("K&M Storage")
    janela.geometry("1150x650")
    janela.resizable(False, False)
    janela.configure(bg="#38b6ff")
    
    # Obter nome do usuário
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM usuarios WHERE email = ?", (email_usuario,))
    nome_usuario = cursor.fetchone()[0]
    conexao.close()

    # Logo no canto superior esquerdo
    try:
        logo_img = PhotoImage(file="logo.png")
        # Redimensionar se necessário (mantendo a referência)
        logo_img = logo_img.subsample(1, 1)  # Ajuste esses valores conforme necessário
        logo_label = tk.Label(janela, image=logo_img, bg="#38b6ff")
        logo_label.place(x=10, y=5)
        # Manter referência para evitar garbage collection
        janela.logo_img = logo_img
    except Exception as e:
        print(f"Erro ao carregar logo: {e}")
        tk.Label(janela, text="K&M Storage", font=("Arial", 16, "bold"), bg="#38b6ff", fg="white").place(x=10, y=10)
    
    try:
        icon_img = PhotoImage(file="icon.png")
        janela.iconphoto(False, icon_img)
        # Manter referência
        janela.icon_img = icon_img
    except Exception as e:
        print(f"Erro ao carregar ícone: {e}")

    # Mensagem de boas-vindas
    tk.Label(janela, text=f"Olá {nome_usuario}, escolha uma da opções abaixo:", 
             font=("Arial", 20, "bold"), bg="#38b6ff", fg="white").place(x=350, y=30)

    # Funções dos botões
    def enviar_mercadoria():
        EnviarMercadoria(janela, email_usuario)

    def retirar_mercadoria():
        RetirarMercadoria(janela, email_usuario)

    def ver_mercadorias():
        VerMercadorias(janela, email_usuario)

    def deletar_conta():
        resposta = messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar sua conta?")
        if resposta:
            try:
                conexao = conectar_banco()
                cursor = conexao.cursor()
                cursor.execute("DELETE FROM usuarios WHERE email = ?", (email_usuario,))
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Sucesso", "Conta deletada com sucesso!")
                janela.destroy()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao deletar conta: {str(e)}")

    def rastrear_mercadoria():
        RastrearMercadoria(janela, email_usuario)

    # Botões principais
    botoes = [
        ("Enviar mercadoria\npara o estoque", "#154360", enviar_mercadoria, (350, 100)),
        ("Retirar mercadoria\ndo estoque", "#154360", retirar_mercadoria, (600, 100)),
        ("Ver suas mercadorias\nestocadas", "#154360", ver_mercadorias, (850, 100)),
        ("Deletar conta", "red", deletar_conta, (750, 500)),
        ("Rastrear mercadoria\n(envio via correios)", "green", rastrear_mercadoria, (35, 425))
    ]

    for texto, cor, comando, posicao in botoes:
        tk.Button(janela, text=texto, font=("Arial", 14, "bold"), bg=cor, fg="white",
                 width=20, height=4, bd=3, relief="solid", command=comando).place(x=posicao[0], y=posicao[1])

    # Aviso lateral
    aviso_frame = tk.Frame(janela, bg="orange", bd=3, relief="solid")
    aviso_frame.place(x=30, y=230, width=260, height=160)
    tk.Label(aviso_frame, text="Aviso!", font=("Arial", 16, "bold"), bg="orange", fg="white").pack(anchor="w", padx=10, pady=(10, 0))
    tk.Label(aviso_frame, text="- Por questão de segurança não\n  é permitida a estocagem de\n  produtos alimentares perecíveis \n  ou inflamáveis/explosivos",
             font=("Arial", 12), bg="orange", fg="white", justify="left").pack(anchor="w", padx=10)

    # Imagem do estoque
    try:
        estoque_img = PhotoImage(file="estoque.png")
        # Redimensionar se necessário
        estoque_img = estoque_img.subsample(1,1)  # Ajuste conforme necessário
        estoque_label = tk.Label(janela, image=estoque_img, bg="#38b6ff")
        estoque_label.place(x=310, y=320)
        # Manter referência
        janela.estoque_img = estoque_img
    except Exception as e:
        print(f"Erro ao carregar imagem do estoque: {e}")
        tk.Label(janela, text="[Imagem do estoque]", bg="#38b6ff", fg="white").place(x=310, y=320)

    # Informacoes do estoque
    info_text = "Informacões do nosso estoque:\n\n- Localização: PR - Curitiba\nAvenida Industrial Nº145"
    tk.Label(janela, text=info_text, font=("Arial", 14, "bold"), bg="#38b6ff", fg="white", justify="left").place(x=740, y=350)
    
    janela.mainloop()