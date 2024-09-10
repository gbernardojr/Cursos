import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import date

# Arquivo JSON para armazenar os chamados
ARQUIVO_CHAMADOS = 'chamados.json'

# Função para carregar os chamados existentes
def carregar_chamados():
    try:
        with open(ARQUIVO_CHAMADOS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função para salvar um novo chamado no arquivo JSON
def salvar_chamados(chamados):
    with open(ARQUIVO_CHAMADOS, 'w') as f:
        json.dump(chamados, f, indent=4)

# Função para gerar o próximo número de chamado
def gerar_numero_chamado():
    chamados = carregar_chamados()
    if chamados:
        ultimo_chamado = chamados[-1]['numero_chamado']
        return ultimo_chamado + 1
    return 1

# Função para salvar o chamado atual
def salvar_chamado():
    nome_cliente = entry_cliente.get()
    tipo_problema = combo_tipo_problema.get()
    descricao = text_descricao.get("1.0", tk.END).strip()
    prioridade = combo_prioridade.get()
    numero_chamado = label_numero_chamado['text']
    data_abertura = label_data_abertura['text']
    
    if not nome_cliente or not tipo_problema or not descricao or not prioridade:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    
    novo_chamado = {
        'numero_chamado': numero_chamado,
        'cliente': nome_cliente,
        'tipo_problema': tipo_problema,
        'descricao': descricao,
        'prioridade': prioridade,
        'data_abertura': data_abertura
    }
    
    chamados = carregar_chamados()
    chamados.append(novo_chamado)
    salvar_chamados(chamados)
    
    messagebox.showinfo("Sucesso", f"Chamado {numero_chamado} salvo com sucesso!")
    novo_chamado_func()

# Função para limpar os campos e preparar para um novo chamado
def novo_chamado_func():
    entry_cliente.delete(0, tk.END)
    combo_tipo_problema.set('')
    text_descricao.delete("1.0", tk.END)
    combo_prioridade.set('')
    label_numero_chamado.config(text=gerar_numero_chamado())
    label_data_abertura.config(text=date.today())

# Função para localizar um chamado pelo número
def localizar_chamado():
    numero_chamado = entry_numero_localizar.get()
    chamados = carregar_chamados()
    
    for chamado in chamados:
        if str(chamado['numero_chamado']) == numero_chamado:
            entry_cliente.delete(0, tk.END)
            entry_cliente.insert(0, chamado['cliente'])
            combo_tipo_problema.set(chamado['tipo_problema'])
            text_descricao.delete("1.0", tk.END)
            text_descricao.insert(tk.END, chamado['descricao'])
            combo_prioridade.set(chamado['prioridade'])
            label_numero_chamado.config(text=chamado['numero_chamado'])
            label_data_abertura.config(text=chamado['data_abertura'])
            return
    
    messagebox.showerror("Erro", f"Chamado {numero_chamado} não encontrado.")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Suporte Técnico")
root.geometry("400x500")

# Configuração do layout da janela com grid

# Label e Entry para o Nome do Cliente
tk.Label(root, text="Nome do Cliente:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

# Combobox para o Tipo de Problema
tk.Label(root, text="Tipo de Problema:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
combo_tipo_problema = ttk.Combobox(root, values=["Problema de Rede", "Falha de Software", "Erro de Hardware"])
combo_tipo_problema.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

# Campo de texto para a Descrição do Problema
tk.Label(root, text="Descrição do Problema:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
text_descricao = tk.Text(root, height=5)
text_descricao.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

# Combobox para Prioridade
tk.Label(root, text="Prioridade:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
combo_prioridade = ttk.Combobox(root, values=["Baixa", "Média", "Alta"])
combo_prioridade.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

# Label para exibir o Número do Chamado
tk.Label(root, text="Número do Chamado:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
label_numero_chamado = tk.Label(root, text=gerar_numero_chamado(), bg='lightgray')
label_numero_chamado.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

# Label para exibir a Data de Abertura
tk.Label(root, text="Data de Abertura:").grid(row=5, column=0, padx=10, pady=5, sticky='w')
label_data_abertura = tk.Label(root, text=date.today(), bg='lightgray')
label_data_abertura.grid(row=5, column=1, padx=10, pady=5, sticky='ew')

# Botão para salvar o chamado
btn_salvar = tk.Button(root, text="Salvar Chamado", command=salvar_chamado)
btn_salvar.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Botão para criar um novo chamado
btn_novo_chamado = tk.Button(root, text="Novo Chamado", command=novo_chamado_func)
btn_novo_chamado.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Campo para inserir o número de chamado a localizar
tk.Label(root, text="Localizar Chamado (Número):").grid(row=8, column=0, padx=10, pady=5, sticky='w')
entry_numero_localizar = tk.Entry(root)
entry_numero_localizar.grid(row=8, column=1, padx=10, pady=5, sticky='ew')

# Botão para localizar o chamado
btn_localizar = tk.Button(root, text="Localizar Chamado", command=localizar_chamado)
btn_localizar.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Expande as colunas para ajustar o layout
root.grid_columnconfigure(1, weight=1)

# Inicia a interface gráfica
root.mainloop()
