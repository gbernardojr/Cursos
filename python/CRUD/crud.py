import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

def atualizar_treeview():
    # Limpar treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Adicionar contatos ordenados por nome
    for id_contato, contato in sorted(contatos.items(), key=lambda item: item[1]['nome']):
        tree.insert("", tk.END, values=(
            id_contato,
            contato['nome'],
            contato['data_nascimento'],
            contato['whatsapp'],
            contato['linkedin'],
            contato['github']
        ))

def adicionar_contato():
    global id_counter
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
#    if data_nasc and not validar_data(data_nasc):
#        messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
#        return
    
    contatos[id_counter] = {
        "nome": nome,
        "data_nascimento": data_nasc if data_nasc else "Não informado",
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    id_counter += 1
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
#    limpar_campos()
    atualizar_treeview()


# Configuração inicial
root = tk.Tk()
root.title("Sistema de Contatos")
root.geometry("800x600")

# Base de dados em dicionário
contatos = {}
id_counter = 1

# Interface gráfica
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Frame de formulário
form_frame = tk.LabelFrame(main_frame, text="Dados do Contato", padx=10, pady=10)
form_frame.pack(fill=tk.X, pady=(0, 10))

# Campos do formulário
tk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky=tk.W)
nome_entry = tk.Entry(form_frame, width=40)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Data Nasc. (DD/MM/AAAA):").grid(row=1, column=0, sticky=tk.W)
data_entry = tk.Entry(form_frame, width=40)
data_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="WhatsApp:").grid(row=2, column=0, sticky=tk.W)
whatsapp_entry = tk.Entry(form_frame, width=40)
whatsapp_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="LinkedIn:").grid(row=3, column=0, sticky=tk.W)
linkedin_entry = tk.Entry(form_frame, width=40)
linkedin_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(form_frame, text="GitHub:").grid(row=4, column=0, sticky=tk.W)
github_entry = tk.Entry(form_frame, width=40)
github_entry.grid(row=4, column=1, padx=5, pady=5)

# Frame de botões
button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=(0, 10))

tk.Button(button_frame, text="Adicionar", command=adicionar_contato).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Atualizar", command=None).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Excluir", command=None).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Limpar", command=None).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Localizar", command=None).pack(side=tk.LEFT, padx=5)

# Treeview para exibir os contatos
tree = ttk.Treeview(main_frame, columns=("ID", "Nome", "Nascimento", "WhatsApp", "LinkedIn", "GitHub"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Nascimento", text="Nascimento")
tree.heading("WhatsApp", text="WhatsApp")
tree.heading("LinkedIn", text="LinkedIn")
tree.heading("GitHub", text="GitHub")

tree.column("ID", width=50)
tree.column("Nome", width=150)
tree.column("Nascimento", width=100)
tree.column("WhatsApp", width=120)
tree.column("LinkedIn", width=150)
tree.column("GitHub", width=150)

tree.pack(fill=tk.BOTH, expand=True)

# Barra de rolagem
scrollbar = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=scrollbar.set)

# Evento de seleção na treeview
tree.bind("<<TreeviewSelect>>",None)  #preencher_campos_selecionados






root.mainloop()




# Funções do CRUD
def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def adicionar_contato():
    global id_counter
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
#    if data_nasc and not validar_data(data_nasc):
#        messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
#        return
    
    contatos[id_counter] = {
        "nome": nome,
        "data_nascimento": data_nasc if data_nasc else "Não informado",
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    id_counter += 1
    messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
#    limpar_campos()
#    atualizar_treeview()

def atualizar_contato():
    item_selecionado = tree.selection()
    
    if not item_selecionado:
        messagebox.showerror("Erro", "Nenhum contato selecionado para atualizar!")
        return
    
    id_contato = int(tree.item(item_selecionado)['values'][0])
    
    nome = nome_entry.get().strip()
    data_nasc = data_entry.get().strip()
    whatsapp = whatsapp_entry.get().strip()
    linkedin = linkedin_entry.get().strip()
    github = github_entry.get().strip()
    
    if not nome:
        messagebox.showerror("Erro", "O campo Nome é obrigatório!")
        return
    
    if data_nasc and not validar_data(data_nasc):
        messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
        return
    
    contatos[id_contato] = {
        "nome": nome,
        "data_nascimento": data_nasc if data_nasc else "Não informado",
        "whatsapp": whatsapp if whatsapp else "Não informado",
        "linkedin": linkedin if linkedin else "Não informado",
        "github": github if github else "Não informado"
    }
    
    messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")
    atualizar_treeview()

def excluir_contato():
    item_selecionado = tree.selection()
    
    if not item_selecionado:
        messagebox.showerror("Erro", "Nenhum contato selecionado para excluir!")
        return
    
    id_contato = int(tree.item(item_selecionado)['values'][0])
    
    if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este contato?"):
        del contatos[id_contato]
        messagebox.showinfo("Sucesso", "Contato excluído com sucesso!")
        limpar_campos()
        atualizar_treeview()

def limpar_campos():
    nome_entry.delete(0, tk.END)
    data_entry.delete(0, tk.END)
    whatsapp_entry.delete(0, tk.END)
    linkedin_entry.delete(0, tk.END)
    github_entry.delete(0, tk.END)

def preencher_campos_selecionados(event):
    item_selecionado = tree.selection()
    
    if item_selecionado:
        valores = tree.item(item_selecionado)['values']
        
        limpar_campos()
        
        nome_entry.insert(0, valores[1])
        data_entry.insert(0, valores[2])
        whatsapp_entry.insert(0, valores[3])
        linkedin_entry.insert(0, valores[4])
        github_entry.insert(0, valores[5])



def carregar_dados_exemplo():
    global id_counter
    exemplos = [
        {"nome": "João Silva", "data_nascimento": "15/05/1990", "whatsapp": "(11) 98765-4321", 
         "linkedin": "linkedin.com/in/joaosilva", "github": "github.com/joaosilva"},
        {"nome": "Maria Souza", "data_nascimento": "22/10/1985", "whatsapp": "(21) 99876-5432", 
         "linkedin": "linkedin.com/in/mariasouza", "github": "github.com/mariasouza"}
    ]
    
    for exemplo in exemplos:
        contatos[id_counter] = exemplo
        id_counter += 1
    
    atualizar_treeview()






# Carregar dados de exemplo
carregar_dados_exemplo()

# Iniciar aplicação
root.mainloop()
