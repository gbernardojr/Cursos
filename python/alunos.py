import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# Conexão com o banco de dados
def conectar():
    conexao = sqlite3.connect('curso_crud.db')
    cursor = conexao.cursor()
    return conexao, cursor

# Criação da tabela de alunos
def criar_tabela():
    conexao, cursor = conectar()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        nascimento TEXT NOT NULL,
                        rg TEXT,
                        cpf TEXT NOT NULL,
                        endereco TEXT,
                        email TEXT,
                        whatsapp TEXT)''')
    conexao.commit()
    conexao.close()

# Função para carregar os alunos no Treeview
def carregar_alunos():
    for item in tree.get_children():
        tree.delete(item)
    conexao, cursor = conectar()
    cursor.execute('SELECT * FROM alunos')
    for aluno in cursor.fetchall():
        tree.insert('', 'end', values=aluno)
    conexao.close()

# Função para adicionar novo aluno
def adicionar_aluno():
    def salvar():
        conexao, cursor = conectar()
        cursor.execute('''INSERT INTO alunos (nome, nascimento, rg, cpf, endereco, email, whatsapp) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (entry_nome.get(), entry_nascimento.get(), entry_rg.get(), entry_cpf.get(),
                        entry_endereco.get(), entry_email.get(), entry_whatsapp.get()))
        conexao.commit()
        conexao.close()
        carregar_alunos()
        janela_adicionar.destroy()

    janela_adicionar = tk.Toplevel()
    janela_adicionar.title("Adicionar Aluno")

    tk.Label(janela_adicionar, text="Nome").grid(row=0, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(janela_adicionar)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_adicionar, text="Nascimento").grid(row=1, column=0, padx=10, pady=5)
    entry_nascimento = tk.Entry(janela_adicionar)
    entry_nascimento.grid(row=1, column=1)

    tk.Label(janela_adicionar, text="RG").grid(row=2, column=0, padx=10, pady=5)
    entry_rg = tk.Entry(janela_adicionar)
    entry_rg.grid(row=2, column=1)

    tk.Label(janela_adicionar, text="CPF").grid(row=3, column=0, padx=10, pady=5)
    entry_cpf = tk.Entry(janela_adicionar)
    entry_cpf.grid(row=3, column=1)

    tk.Label(janela_adicionar, text="Endereço").grid(row=4, column=0, padx=10, pady=5)
    entry_endereco = tk.Entry(janela_adicionar)
    entry_endereco.grid(row=4, column=1)

    tk.Label(janela_adicionar, text="E-mail").grid(row=5, column=0, padx=10, pady=5)
    entry_email = tk.Entry(janela_adicionar)
    entry_email.grid(row=5, column=1)

    tk.Label(janela_adicionar, text="WhatsApp").grid(row=6, column=0, padx=10, pady=5)
    entry_whatsapp = tk.Entry(janela_adicionar)
    entry_whatsapp.grid(row=6, column=1)

    tk.Button(janela_adicionar, text="Salvar", command=salvar).grid(row=7, column=0, columnspan=2, pady=10)

# Função para excluir aluno
def excluir_aluno():
    selecionado = tree.selection()
    if selecionado:
        aluno_id = tree.item(selecionado[0])['values'][0]
        conexao, cursor = conectar()
        cursor.execute('DELETE FROM alunos WHERE id = ?', (aluno_id,))
        conexao.commit()
        conexao.close()
        carregar_alunos()
    else:
        messagebox.showwarning("Aviso", "Selecione um aluno para excluir!")

# Função para editar aluno ao clicar duas vezes no registro
def editar_aluno(event):
    selecionado = tree.selection()
    if selecionado:
        aluno_id = tree.item(selecionado[0])['values'][0]
        conexao, cursor = conectar()
        cursor.execute('SELECT * FROM alunos WHERE id = ?', (aluno_id,))
        aluno = cursor.fetchone()
        conexao.close()

        def salvar_edicao():
            conexao, cursor = conectar()
            cursor.execute('''UPDATE alunos SET nome = ?, nascimento = ?, rg = ?, cpf = ?, endereco = ?, email = ?, whatsapp = ?
                              WHERE id = ?''',
                           (entry_nome.get(), entry_nascimento.get(), entry_rg.get(), entry_cpf.get(),
                            entry_endereco.get(), entry_email.get(), entry_whatsapp.get(), aluno_id))
            conexao.commit()
            conexao.close()
            carregar_alunos()
            janela_editar.destroy()

        janela_editar = tk.Toplevel()
        janela_editar.title("Editar Aluno")

        tk.Label(janela_editar, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        entry_nome = tk.Entry(janela_editar)
        entry_nome.grid(row=0, column=1)
        entry_nome.insert(0, aluno[1])

        tk.Label(janela_editar, text="Nascimento").grid(row=1, column=0, padx=10, pady=5)
        entry_nascimento = tk.Entry(janela_editar)
        entry_nascimento.grid(row=1, column=1)
        entry_nascimento.insert(0, aluno[2])

        tk.Label(janela_editar, text="RG").grid(row=2, column=0, padx=10, pady=5)
        entry_rg = tk.Entry(janela_editar)
        entry_rg.grid(row=2, column=1)
        entry_rg.insert(0, aluno[3])

        tk.Label(janela_editar, text="CPF").grid(row=3, column=0, padx=10, pady=5)
        entry_cpf = tk.Entry(janela_editar)
        entry_cpf.grid(row=3, column=1)
        entry_cpf.insert(0, aluno[4])

        tk.Label(janela_editar, text="Endereço").grid(row=4, column=0, padx=10, pady=5)
        entry_endereco = tk.Entry(janela_editar)
        entry_endereco.grid(row=4, column=1)
        entry_endereco.insert(0, aluno[5])

        tk.Label(janela_editar, text="E-mail").grid(row=5, column=0, padx=10, pady=5)
        entry_email = tk.Entry(janela_editar)
        entry_email.grid(row=5, column=1)
        entry_email.insert(0, aluno[6])

        tk.Label(janela_editar, text="WhatsApp").grid(row=6, column=0, padx=10, pady=5)
        entry_whatsapp = tk.Entry(janela_editar)
        entry_whatsapp.grid(row=6, column=1)
        entry_whatsapp.insert(0, aluno[7])

        tk.Button(janela_editar, text="Salvar", command=salvar_edicao).grid(row=7, column=0, columnspan=2, pady=10)

# Configuração da interface principal
root = tk.Tk()
root.title("CRUD de Alunos")

# Tabela para exibir os alunos
tree = ttk.Treeview(root, columns=('ID', 'Nome', 'Nascimento', 'RG', 'CPF', 'Endereço', 'E-mail', 'WhatsApp'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Nome', text='Nome')
tree.heading('Nascimento', text='Nascimento')
tree.heading('RG', text='RG')
tree.heading('CPF', text='CPF')
tree.heading('Endereço', text='Endereço')
tree.heading('E-mail', text='E-mail')
tree.heading('WhatsApp', text='WhatsApp')
tree.grid(row=0, column=0, columnspan=4)

tree.bind('<Double-1>', editar_aluno)

# Botões de adicionar e excluir
btn_adicionar = tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno)
btn_adicionar.grid(row=1, column=0, pady=10, padx=10)

btn_excluir = tk.Button(root, text="Excluir Aluno", command=excluir_aluno)
btn_excluir.grid(row=1, column=1, pady=10, padx=10)

# Carrega os dados ao iniciar o programa
criar_tabela()
carregar_alunos()

root.mainloop()
