import tkinter as tk
from tkinter import PhotoImage

# Função principal da interface
def abrir_pagina_principal():
    janela = tk.Tk()
    janela.title("K&M Storage")
    janela.geometry("1150x650")
    janela.resizable(False,False)
    janela.configure(bg="#38b6ff")

    # Logo no canto superior esquerdo
    try:
        logo = PhotoImage(file="icon.png")
        tk.Label(janela, image=logo, bg="#38b6ff").place(x=10, y=5)
    except:
        tk.Label(janela, text="K&M Storage", font=("Arial", 16, "bold"), bg="#38b6ff", fg="white").place(x=10, y=10)

    # Mensagem de boas-vindas
    tk.Label(janela, text="Olá Rafael, escolha uma da opções abaixo:", font=("Arial", 20, "bold"), bg="#38b6ff", fg="white").place(x=350, y=30)

    # Botões principais
    tk.Button(janela, text="Enviar produto\npara o estoque", font=("Arial", 14, "bold"), bg="#154360", fg="white",
              width=20, height=4, bd=3, relief="solid").place(x=350, y=100)

    tk.Button(janela, text="Retirar produto\ndo estoque", font=("Arial", 14, "bold"), bg="red", fg="white",
              width=20, height=4, bd=3, relief="solid").place(x=600, y=100)

    tk.Button(janela, text="Rastrear seu produto", font=("Arial", 14, "bold"), bg="#154360", fg="white",
              width=20, height=4, bd=3, relief="solid").place(x=850, y=100)

    # Aviso lateral
    aviso_frame = tk.Frame(janela, bg="orange", bd=3, relief="solid")
    aviso_frame.place(x=30, y=230, width=260, height=160)
    tk.Label(aviso_frame, text="Aviso!", font=("Arial", 16, "bold"), bg="orange", fg="white").pack(anchor="w", padx=10, pady=(10, 0))
    tk.Label(aviso_frame, text="- Por questão de segurança não\n  é permitida a estocagem de\n  produtos alimentares perecíveis \n  ou inflamáveis/explosivos",
             font=("Arial", 12), bg="orange", fg="white", justify="left").pack(anchor="w", padx=10)

    # Imagem do estoque
    try:
        estoque_img = PhotoImage(file="estoque.png")  # salve como estoque.png
        tk.Label(janela, image=estoque_img).place(x=310, y=320)
    except:
        tk.Label(janela, text="[Imagem do estoque]", bg="#38b6ff", fg="white").place(x=310, y=320)

    # Informacoes do estoque
    info_text = "Informacões do nosso estoque:\n\n- Localização: PR - Curitiba\nAvenida Industrial Nº145"
    tk.Label(janela, text=info_text, font=("Arial", 14, "bold"), bg="#38b6ff", fg="white", justify="left").place(x=740, y=350)

    janela.mainloop()

# Para testes locais
if __name__ == "__main__":
    abrir_pagina_principal()
