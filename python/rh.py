import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('funcionarios.db')
cursor = conexao.cursor()

# Cria a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER,
                    cargo TEXT,
                    departamento TEXT,
                    salario REAL,
                    telefone TEXT,
                    email TEXT)''')
conexao.commit()


def atualizar_lista(nome):
    ...


# Interface gráfica com Tkinter
janelaPrincipal = tk.Tk()
janelaPrincipal.title("CRUD de Funcionários")

# Campo de pesquisa
tk.Label(janelaPrincipal, text="Pesquisar por Nome:").grid(row=0, column=0, 
                                                           padx=10, pady=10)
entry_pesquisa = tk.Entry(janelaPrincipal)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRelease>", lambda event: atualizar_lista(entry_pesquisa.get()))

# Botões
btn_adicionar = tk.Button(janelaPrincipal, text="Adicionar", command='')
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(janelaPrincipal, text="Alterar", command='')
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(janelaPrincipal, text="Deletar", command='')
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

# Grid (Treeview) para exibir a lista de funcionários
tree = ttk.Treeview(janelaPrincipal, columns=("ID", "Nome", "Idade", "Cargo", "Departamento", "Salário", "Telefone", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Funcionário")
tree.heading("Idade", text="Idade")
tree.heading("Cargo", text="Cargo")
tree.heading("Departamento", text="Departamento")
tree.heading("Salário", text="Salário")
tree.heading("Telefone", text="Telefone")
tree.heading("Email", text="Email")
tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10)






janelaPrincipal.mainloop()
