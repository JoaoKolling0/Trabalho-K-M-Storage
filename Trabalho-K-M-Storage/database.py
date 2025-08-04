import sqlite3
from datetime import datetime

def conectar_banco():
    conexao = sqlite3.connect("banco.db")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        email TEXT PRIMARY KEY,
        nome TEXT,
        senha TEXT
    )''')

    # Mercadorias
    cursor.execute('''CREATE TABLE IF NOT EXISTS mercadorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_email TEXT,
        nome TEXT,
        quantidade INTEGER,
        data_entrada TEXT,
        codigo_rastreio TEXT,
        FOREIGN KEY(usuario_email) REFERENCES usuarios(email)
    )''')

    # Histórico de retiradas
    cursor.execute('''CREATE TABLE IF NOT EXISTS retiradas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_email TEXT,
        nome_mercadoria TEXT,
        quantidade INTEGER,
        data_retirada TEXT,
        FOREIGN KEY(usuario_email) REFERENCES usuarios(email)
    )''')

    conexao.commit()
    conexao.close()
# Funções para mercadorias
def adicionar_mercadoria(email, nome, quantidade, codigo_rastreio=None):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    cursor.execute("INSERT INTO mercadorias (usuario_email, nome, quantidade, data_entrada, codigo_rastreio) VALUES (?, ?, ?, ?, ?)",
                   (email, nome, quantidade, data_atual, codigo_rastreio))
    conexao.commit()
    conexao.close()

def retirar_mercadoria(email, nome, quantidade):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Verifica se há quantidade suficiente
    cursor.execute("SELECT quantidade FROM mercadorias WHERE usuario_email = ? AND nome = ?", (email, nome))
    resultado = cursor.fetchone()
    
    if not resultado:
        conexao.close()
        return False, "Mercadoria não encontrada"
    
    if resultado[0] < quantidade:
        conexao.close()
        return False, "Quantidade insuficiente em estoque"
    
    # Atualiza o estoque
    cursor.execute("UPDATE mercadorias SET quantidade = quantidade - ? WHERE usuario_email = ? AND nome = ?",
                   (quantidade, email, nome))
    
    # Registra a retirada no histórico
    cursor.execute("INSERT INTO retiradas (usuario_email, nome_mercadoria, quantidade, data_retirada) VALUES (?, ?, ?, ?)",
                   (email, nome, quantidade, data_atual))
    
    conexao.commit()
    conexao.close()
    return True, "Retirada realizada com sucesso"

def listar_mercadorias(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, quantidade, data_entrada, codigo_rastreio FROM mercadorias WHERE usuario_email = ?", (email,))
    dados = cursor.fetchall()
    conexao.close()
    return dados

def buscar_por_rastreio(email, codigo):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, quantidade, data_entrada FROM mercadorias WHERE usuario_email = ? AND codigo_rastreio = ?", 
                   (email, codigo))
    dados = cursor.fetchall()
    conexao.close()
    return dados