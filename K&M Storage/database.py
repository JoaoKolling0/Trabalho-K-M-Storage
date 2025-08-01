import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("banco.db")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                   (email TEXT PRIMARY KEY, nome TEXT, senha TEXT)''')
    
    conexao.commit()