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

# Função para buscar funcionários no banco de dados
def buscar_funcionarios(nome=""):
    cursor.execute("SELECT * FROM funcionarios WHERE nome LIKE ?", ('%' + nome + '%',))
    return cursor.fetchall()

# Função para atualizar o grid com a lista de funcionários
def atualizar_lista(nome=""):
    for row in tree.get_children():
        tree.delete(row)
    funcionarios = buscar_funcionarios(nome)
    for funcionario in funcionarios:
        tree.insert("", "end", values=funcionario)

# Função para adicionar um funcionário ao banco de dados
def adicionar_funcionario():
    def salvar_funcionario():
        nome = entry_nome.get()
        idade = entry_idade.get()
        cargo = entry_cargo.get()
        departamento = entry_departamento.get()
        salario = entry_salario.get()
        telefone = entry_telefone.get()
        email = entry_email.get()

        if nome and idade and cargo and departamento and salario and telefone and email:
            cursor.execute("INSERT INTO funcionarios (nome, idade, cargo, departamento, salario, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                           (nome, idade, cargo, departamento, salario, telefone, email))
            conexao.commit()
            atualizar_lista()
            janela_add.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    # Janela para adicionar funcionário
    janela_add = tk.Toplevel(root)
    janela_add.title("Adicionar Funcionário")
    
    # Campos de entrada
    tk.Label(janela_add, text="Nome").grid(row=0, column=0)
    entry_nome = tk.Entry(janela_add)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_add, text="Idade").grid(row=1, column=0)
    entry_idade = tk.Entry(janela_add)
    entry_idade.grid(row=1, column=1)

    tk.Label(janela_add, text="Cargo").grid(row=2, column=0)
    entry_cargo = tk.Entry(janela_add)
    entry_cargo.grid(row=2, column=1)

    tk.Label(janela_add, text="Departamento").grid(row=3, column=0)
    entry_departamento = tk.Entry(janela_add)
    entry_departamento.grid(row=3, column=1)

    tk.Label(janela_add, text="Salário").grid(row=4, column=0)
    entry_salario = tk.Entry(janela_add)
    entry_salario.grid(row=4, column=1)

    tk.Label(janela_add, text="Telefone").grid(row=5, column=0)
    entry_telefone = tk.Entry(janela_add)
    entry_telefone.grid(row=5, column=1)

    tk.Label(janela_add, text="Email").grid(row=6, column=0)
    entry_email = tk.Entry(janela_add)
    entry_email.grid(row=6, column=1)

    # Botão para salvar o funcionário
    btn_salvar = tk.Button(janela_add, text="Salvar", command=salvar_funcionario)
    btn_salvar.grid(row=7, columnspan=2)

# Função para deletar um funcionário do banco de dados
def deletar_funcionario():
    item_selecionado = tree.selection()
    if item_selecionado:
        funcionario = tree.item(item_selecionado)['values']
        cursor.execute("DELETE FROM funcionarios WHERE id=?", (funcionario[0],))
        conexao.commit()
        atualizar_lista()
    else:
        messagebox.showerror("Erro", "Selecione um funcionário para deletar.")

# Função para alterar um funcionário
def alterar_funcionario():
    item_selecionado = tree.selection()
    if item_selecionado:
        funcionario = tree.item(item_selecionado)['values']

        def salvar_alteracao():
            nome = entry_nome.get()
            idade = entry_idade.get()
            cargo = entry_cargo.get()
            departamento = entry_departamento.get()
            salario = entry_salario.get()
            telefone = entry_telefone.get()
            email = entry_email.get()

            cursor.execute("UPDATE funcionarios SET nome=?, idade=?, cargo=?, departamento=?, salario=?, telefone=?, email=? WHERE id=?", 
                           (nome, idade, cargo, departamento, salario, telefone, email, funcionario[0]))
            conexao.commit()
            atualizar_lista()
            janela_editar.destroy()

        # Janela para editar funcionário
        janela_editar = tk.Toplevel(root)
        janela_editar.title("Alterar Funcionário")

        # Campos de entrada
        tk.Label(janela_editar, text="Nome").grid(row=0, column=0)
        entry_nome = tk.Entry(janela_editar)
        entry_nome.insert(0, funcionario[1])
        entry_nome.grid(row=0, column=1)

        tk.Label(janela_editar, text="Idade").grid(row=1, column=0)
        entry_idade = tk.Entry(janela_editar)
        entry_idade.insert(0, funcionario[2])
        entry_idade.grid(row=1, column=1)

        tk.Label(janela_editar, text="Cargo").grid(row=2, column=0)
        entry_cargo = tk.Entry(janela_editar)
        entry_cargo.insert(0, funcionario[3])
        entry_cargo.grid(row=2, column=1)

        tk.Label(janela_editar, text="Departamento").grid(row=3, column=0)
        entry_departamento = tk.Entry(janela_editar)
        entry_departamento.insert(0, funcionario[4])
        entry_departamento.grid(row=3, column=1)

        tk.Label(janela_editar, text="Salário").grid(row=4, column=0)
        entry_salario = tk.Entry(janela_editar)
        entry_salario.insert(0, funcionario[5])
        entry_salario.grid(row=4, column=1)

        tk.Label(janela_editar, text="Telefone").grid(row=5, column=0)
        entry_telefone = tk.Entry(janela_editar)
        entry_telefone.insert(0, funcionario[6])
        entry_telefone.grid(row=5, column=1)

        tk.Label(janela_editar, text="Email").grid(row=6, column=0)
        entry_email = tk.Entry(janela_editar)
        entry_email.insert(0, funcionario[7])
        entry_email.grid(row=6, column=1)

        # Botão para salvar alterações
        btn_salvar = tk.Button(janela_editar, text="Salvar", command=salvar_alteracao)
        btn_salvar.grid(row=7, columnspan=2)
    else:
        messagebox.showerror("Erro", "Selecione um funcionário para alterar.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("CRUD de Funcionários")

# Campo de pesquisa
tk.Label(root, text="Pesquisar por Nome:").grid(row=0, column=0, padx=10, pady=10)
entry_pesquisa = tk.Entry(root)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRelease>", lambda event: atualizar_lista(entry_pesquisa.get()))

# Botões
btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar_funcionario)
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(root, text="Alterar", command=alterar_funcionario)
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(root, text="Deletar", command=deletar_funcionario)
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

# Grid (Treeview) para exibir a lista de funcionários
tree = ttk.Treeview(root, columns=("ID", "Nome", "Idade", "Cargo", "Departamento", "Salário", "Telefone", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Cargo", text="Cargo")
tree.heading("Departamento", text="Departamento")
tree.heading("Salário", text="Salário")
tree.heading("Telefone", text="Telefone")
tree.heading("Email", text="Email")
tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Atualiza o grid inicialmente
atualizar_lista()

# Executa a interface
root.mainloop()



# Fechar a conexão com o banco de dados ao encerrar o programa
conexao.close()
