import tkinter as tk
from tkinter import messagebox

# Sistema de Gerenciamento de Estoque - Ambiente Gráfico

# Função para adicionar um produto ao estoque
def adicionar_produto():
    nome_produto = entry_nome.get()
    quantidade = entry_quantidade.get()
    
    if nome_produto and quantidade.isdigit():
        quantidade = int(quantidade)
        if quantidade >= 0:
            if nome_produto in estoque:
                messagebox.showinfo("Erro", f'O produto "{nome_produto}" já está no estoque.')
            else:
                estoque[nome_produto] = quantidade
                atualizar_lista_estoque()
                limpar_campos()
                messagebox.showinfo("Sucesso", f'Produto "{nome_produto}" adicionado com sucesso!')
        else:
            messagebox.showinfo("Erro", "A quantidade deve ser maior ou igual a zero.")
    else:
        messagebox.showinfo("Erro", "Nome do produto ou quantidade inválidos!")
    

# Função para atualizar a quantidade de um produto
def atualizar_lista_estoque():
    listbox_estoque.delete(0, tk.END)
    if estoque:
        for produto, quantidade in estoque.items():
            listbox_estoque.insert(tk.END, f"{produto}: {quantidade} unidade(s)")
    else:
        listbox_estoque.insert(tk.END, "Estoque vazio.")
        
# Função para remover um produto do estoque
def remover_produto():
    ..

# Função para atualizar a lista de produtos no Listbox
def atualizar_lista_estoque():
    ...

# Função para limpar os campos de entrada
def limpar_campos():
    ...

# Dicionário para armazenar o estoque
estoque = {}

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerenciamento de Estoque")

# Labels
label_nome = tk.Label(janela, text="Nome do Produto:")
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_quantidade = tk.Label(janela, text="Quantidade:")
label_quantidade.grid(row=1, column=0, padx=10, pady=10)

# Campos de Entrada
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=1, column=1, padx=10, pady=10)

# Botões
btn_adicionar = tk.Button(janela, text="Adicionar Produto", command=adicionar_produto)
btn_adicionar.grid(row=2, column=0, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text="Atualizar Quantidade", command=atualizar_quantidade)
btn_atualizar.grid(row=2, column=1, padx=10, pady=10)

btn_remover = tk.Button(janela, text="Remover Produto", command=remover_produto)
btn_remover.grid(row=2, column=2, padx=10, pady=10)

# Listbox para exibir o estoque
listbox_estoque = tk.Listbox(janela, width=50, height=10)
listbox_estoque.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Inicializar a lista de estoque
atualizar_lista_estoque()

# Iniciar o loop principal da interface
janela.mainloop()
