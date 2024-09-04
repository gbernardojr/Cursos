import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Função para calcular o total do pedido
def calcular_total():
    try:
        quantidade = int(entry_quantidade.get())
        preco_unitario = float(entry_preco.get())
        preco_total = quantidade * preco_unitario
        label_total_valor.config(text=f"R$ {preco_total:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para quantidade e preço!")

# Função para salvar o pedido em um arquivo JSON
def salvar_pedido():
    nome_lanche = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco_unitario = entry_preco.get()

    if not nome_lanche or not quantidade or not preco_unitario:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        quantidade = int(quantidade)
        preco_unitario = float(preco_unitario)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser número inteiro e preço deve ser um número!")
        return

    preco_total = quantidade * preco_unitario

    # Estrutura do pedido
    pedido = {
        "nome_lanche": nome_lanche,
        "quantidade": quantidade,
        "preco_unitario": preco_unitario,
        "preco_total": preco_total
    }

    # Verifica se o arquivo JSON já existe
    if os.path.exists("pedidos.json"):
        with open("pedidos.json", "r") as arquivo:
            pedidos = json.load(arquivo)
    else:
        pedidos = []

    # Adiciona o novo pedido
    pedidos.append(pedido)

    # Salva no arquivo JSON
    with open("pedidos.json", "w") as arquivo:
        json.dump(pedidos, arquivo, indent=4)

    messagebox.showinfo("Sucesso", "Pedido salvo com sucesso!")

    # Limpa os campos após salvar
    limpar_campos()

# Função para exibir um pedido específico
def recuperar_pedido():
    if os.path.exists("pedidos.json"):
        nome_lanche = simpledialog.askstring("Recuperar Pedido", "Digite o nome do lanche:")
        if not nome_lanche:
            return

        with open("pedidos.json", "r") as arquivo:
            pedidos = json.load(arquivo)

        # Procura o pedido pelo nome do lanche
        for pedido in pedidos:
            if pedido["nome_lanche"].lower() == nome_lanche.lower():
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, pedido["nome_lanche"])
                entry_quantidade.delete(0, tk.END)
                entry_quantidade.insert(0, pedido["quantidade"])
                entry_preco.delete(0, tk.END)
                entry_preco.insert(0, pedido["preco_unitario"])
                label_total_valor.config(text=f"R$ {pedido['preco_total']:.2f}")
                return

        messagebox.showinfo("Pedido não encontrado", f"Pedido com nome '{nome_lanche}' não encontrado.")
    else:
        messagebox.showinfo("Sem Pedidos", "Nenhum pedido cadastrado até o momento.")

# Função para limpar os campos
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    label_total_valor.config(text="R$ 0.00")
    entry_nome.focus()

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Pedidos de Lanches")

# Labels e Entries para os campos
label_nome = tk.Label(janela, text="Nome do Lanche")
label_nome.grid(row=0, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

label_quantidade = tk.Label(janela, text="Quantidade")
label_quantidade.grid(row=1, column=0)

entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=1, column=1)

label_preco = tk.Label(janela, text="Preço Unitário")
label_preco.grid(row=2, column=0)

entry_preco = tk.Entry(janela)
entry_preco.grid(row=2, column=1)

# Label para exibir o total do pedido
label_total = tk.Label(janela, text="Total do Pedido")
label_total.grid(row=3, column=0)

label_total_valor = tk.Label(janela, text="R$ 0.00")
label_total_valor.grid(row=3, column=1)

# Botões organizados em duas linhas
botao_calcular = tk.Button(janela, text="Calcular Total", width=20, command=calcular_total)
botao_calcular.grid(row=4, column=0)

botao_salvar = tk.Button(janela, text="Salvar Pedido", width=20, command=salvar_pedido)
botao_salvar.grid(row=4, column=1)

botao_recuperar = tk.Button(janela, text="Recuperar Pedido", width=20, command=recuperar_pedido)
botao_recuperar.grid(row=5, column=0)

botao_novo_pedido = tk.Button(janela, text="Novo Pedido", width=20, command=limpar_campos)
botao_novo_pedido.grid(row=5, column=1)

janela.mainloop()
