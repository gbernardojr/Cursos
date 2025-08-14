import tkinter as tk
from tkinter import messagebox
import json
import os

# Nome do arquivo JSON
ARQUIVO_JSON = "livros.json"

def limpar_campos():
    """Limpa todos os campos de entrada"""
    entryNomeLivro.delete(0, tk.END)
    entryNomeAutor.delete(0, tk.END)
    entryNomeEditora.delete(0, tk.END)
    entryAnoPublicacao.delete(0, tk.END)
    entryDataCompra.delete(0, tk.END)
    entryQtdePaginas.delete(0, tk.END)

def preencher_campos(livro):
    """Preenche os campos com os dados de um livro"""
    limpar_campos()
    entryNomeLivro.insert(0, livro.get("nome", ""))
    entryNomeAutor.insert(0, livro.get("autor", ""))
    entryNomeEditora.insert(0, livro.get("editora", ""))
    entryAnoPublicacao.insert(0, livro.get("ano_publicacao", ""))
    entryDataCompra.insert(0, livro.get("data_compra", ""))
    entryQtdePaginas.insert(0, livro.get("paginas", ""))

def carregar_livros():
    """Carrega os livros do arquivo JSON ou retorna lista vazia se não existir"""
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def salvar_livros(livros):
    """Salva a lista de livros no arquivo JSON"""
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(livros, f, ensure_ascii=False, indent=4)

def Cadastrar():
    """Função para cadastrar um novo livro"""
    # Obter os valores dos campos
    livro = {
        "nome": entryNomeLivro.get(),
        "autor": entryNomeAutor.get(),
        "editora": entryNomeEditora.get(),
        "ano_publicacao": entryAnoPublicacao.get(),
        "data_compra": entryDataCompra.get(),
        "paginas": entryQtdePaginas.get()
    }
    
    # Validar campos obrigatórios
    if not livro["nome"] or not livro["autor"]:
        messagebox.showwarning("Aviso", "Nome do livro e autor são obrigatórios!")
        return
    
    # Carregar livros existentes
    livros = carregar_livros()
    
    # Adicionar novo livro
    livros.append(livro)
    
    # Salvar no arquivo
    salvar_livros(livros)
    
    # Mostrar mensagem de sucesso
    messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
    
    # Limpar campos (opcional)
    entryNomeLivro.delete(0, tk.END)
    entryNomeAutor.delete(0, tk.END)
    entryNomeEditora.delete(0, tk.END)
    entryAnoPublicacao.delete(0, tk.END)
    entryDataCompra.delete(0, tk.END)
    entryQtdePaginas.delete(0, tk.END)

def Pesquisar():
    """Função para pesquisar livros por nome"""
    nome_livro = entryNomeLivro.get()
    if not nome_livro:
        messagebox.showwarning("Aviso", "Digite o nome do livro para pesquisar!")
        return
    
    livros = carregar_livros()
    
    # Loop tradicional em vez de list comprehension
    resultados = []
    for livro in livros:
        if nome_livro.lower() in livro["nome"].lower():
            resultados.append(livro)
    
    if not resultados:
        messagebox.showinfo("Resultado", "Nenhum livro encontrado com este nome!")
        return
    
    # Mostrar o primeiro resultado encontrado
    livro = resultados[0]
    preencher_campos(livro)
    
    messagebox.showinfo("Resultado", f"{len(resultados)} livro(s) encontrado(s). Dados do primeiro exibidos.")


# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Livros")
janela.geometry("400x300")

# Nome do Livro
labelNomeLivro = tk.Label(janela, text='Nome Livro', width=15)
labelNomeLivro.grid(row=0, column=0, padx=5, pady=5)
entryNomeLivro = tk.Entry(janela, width=25)
entryNomeLivro.grid(row=0, column=1, padx=5, pady=5)

# Nome do Autor
labelNomeAutor = tk.Label(janela, text='Nome Autor')
labelNomeAutor.grid(row=1, column=0, padx=5, pady=5)
entryNomeAutor = tk.Entry(janela, width=25)
entryNomeAutor.grid(row=1, column=1, padx=5, pady=5)

# Nome da Editora
labelNomeEditora = tk.Label(janela, text='Nome Editora')
labelNomeEditora.grid(row=2, column=0, padx=5, pady=5)
entryNomeEditora = tk.Entry(janela, width=25)
entryNomeEditora.grid(row=2, column=1, padx=5, pady=5)

# Ano Publicação
labelAnoPublicacao = tk.Label(janela, text='Ano Publicação')
labelAnoPublicacao.grid(row=3, column=0, padx=5, pady=5)
entryAnoPublicacao = tk.Entry(janela, width=25)
entryAnoPublicacao.grid(row=3, column=1, padx=5, pady=5)

# Data Compra
labelDataCompra = tk.Label(janela, text='Data Compra')
labelDataCompra.grid(row=4, column=0, padx=5, pady=5)
entryDataCompra = tk.Entry(janela, width=25)
entryDataCompra.grid(row=4, column=1, padx=5, pady=5)

# Quantidade Páginas
labelQtdePaginas = tk.Label(janela, text='Qtde páginas')
labelQtdePaginas.grid(row=5, column=0, padx=5, pady=5)
entryQtdePaginas = tk.Entry(janela, width=25)
entryQtdePaginas.grid(row=5, column=1, padx=5, pady=5)

# Botão Cadastrar
buttonCadastrar = tk.Button(janela, text='Cadastrar', width=20, command=Cadastrar)
buttonCadastrar.grid(row=6, column=0, columnspan=2, pady=10)

# Botões secundários (sem funcionalidade implementada)
buttonApagar = tk.Button(janela, text='Apagar', width=20)
buttonApagar.grid(row=7, column=0, padx=5, pady=5)

buttonPesquisar = tk.Button(janela, text='Pesquisar', width=20)
buttonPesquisar.grid(row=7, column=1, padx=5, pady=5)

buttonAlterar = tk.Button(janela, text='Alterar', width=20)
buttonAlterar.grid(row=8, column=0, columnspan=2, pady=5)

janela.mainloop()
