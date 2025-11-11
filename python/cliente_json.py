import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
import os

# Nome do arquivo JSON
ARQUIVO_JSON = "banco_dados.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON se existir"""
    global BancoDados
    try:
        if os.path.exists(ARQUIVO_JSON):
            with open(ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
                BancoDados = json.load(arquivo)
        else:
            BancoDados = []
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao carregar dados: {str(e)}')
        BancoDados = []

def salvar_dados():
    """Salva os dados no arquivo JSON"""
    try:
        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
            json.dump(BancoDados, arquivo, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao salvar dados: {str(e)}')
        return False

def fnovo():
    """Limpa os campos para novo cadastro"""
    entCodigo.delete(0, tk.END)
    entDataNasc.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entNome.delete(0, tk.END)

def fgravar():
    """Grava um novo registro ou atualiza um existente"""
    if not entCodigo.get():
        messagebox.showerror('Campo obrigatório', 'Código')
        return
    
    codigo = entCodigo.get().strip()
    registro = { 
        'Codigo': codigo,
        'Nome': entNome.get().strip(),
        'Nascimento': entDataNasc.get().strip(),
        'Email': entEmail.get().strip()
    }

    # Verifica se o código já existe para atualização
    codigo_existente = False
    for i, reg in enumerate(BancoDados):
        if reg['Codigo'] == codigo:
            BancoDados[i] = registro  # Atualiza registro existente
            codigo_existente = True
            break
    
    if not codigo_existente:
        BancoDados.append(registro)  # Adiciona novo registro

    if salvar_dados():
        messagebox.showinfo('Sucesso', 'Gravação realizada com sucesso!')
        fnovo()

def fbusca():
    """Busca um registro pelo nome"""
    nome = simpledialog.askstring('Busca', 'Nome da pessoa para localizar no banco de dados:')
    
    if nome:
        nome = nome.strip()
        encontrados = []
        
        for registro in BancoDados:
            if nome.lower() in registro['Nome'].lower():
                encontrados.append(registro)
        
        if len(encontrados) == 1:
            # Se encontrou apenas um, preenche os campos
            registro = encontrados[0]
            fnovo()
            entCodigo.insert(0, registro['Codigo'])
            entNome.insert(0, registro['Nome'])
            entDataNasc.insert(0, registro['Nascimento'])
            entEmail.insert(0, registro['Email'])
        elif len(encontrados) > 1:
            # Se encontrou múltiplos, mostra lista para seleção
            selecionar_registro(encontrados)
        else:
            messagebox.showinfo('Busca', 'Nenhum registro encontrado.')

def selecionar_registro(registros):
    """Cria uma janela para selecionar entre múltiplos registros encontrados"""
    janela_selecao = tk.Toplevel(janela)
    janela_selecao.title('Selecionar Registro')
    janela_selecao.geometry('600x400')
    
    tk.Label(janela_selecao, text='Múltiplos registros encontrados. Selecione um:', 
             font=('Calibri', 16)).pack(pady=10)
    
    lista_frame = tk.Frame(janela_selecao)
    lista_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    for i, registro in enumerate(registros):
        texto = f"Código: {registro['Codigo']} | Nome: {registro['Nome']} | Email: {registro['Email']}"
        btn = tk.Button(lista_frame, text=texto, font=('Calibri', 12), 
                       command=lambda r=registro: preencher_e_fechar(r, janela_selecao))
        btn.pack(fill='x', pady=2)

def preencher_e_fechar(registro, janela_selecao):
    """Preenche os campos com o registro selecionado e fecha a janela"""
    fnovo()
    entCodigo.insert(0, registro['Codigo'])
    entNome.insert(0, registro['Nome'])
    entDataNasc.insert(0, registro['Nascimento'])
    entEmail.insert(0, registro['Email'])
    janela_selecao.destroy()

def fExcluir():
    """Exclui um registro"""
    codigo = entCodigo.get().strip()
    if not codigo:
        messagebox.showwarning('Aviso', 'Nenhum código informado para exclusão.')
        return
    
    for registro in BancoDados:
        if registro['Codigo'] == codigo:
            if messagebox.askyesno('Confirmar', f'Deseja realmente excluir {registro["Nome"]}?'):
                BancoDados.remove(registro)
                if salvar_dados():
                    messagebox.showinfo('Excluir', f'{registro["Nome"]} excluído com sucesso!')
                    fnovo()
            return
    
    messagebox.showinfo('Excluir', 'Registro não encontrado.')

# Inicialização da aplicação
janela = tk.Tk()
janela.geometry('800x600')
janela.title('Cadastro de Cliente - Com Persistência JSON')
janela.resizable(True, True)

# Carrega os dados do arquivo JSON ao iniciar
carregar_dados()

tamanhoFonte = 28
fonte = 'Calibri'

#*********************************************
frame1 = tk.Frame(janela)
frame1.pack(pady=5)

lblCodigo = tk.Label(frame1, text='Código', font=(fonte, tamanhoFonte))
lblCodigo.grid(row=0, column=0, padx=5, pady=5)
entCodigo = tk.Entry(frame1, font=(fonte, tamanhoFonte))
entCodigo.grid(row=0, column=1)

lblNome = tk.Label(frame1, text='Nome', font=(fonte, tamanhoFonte))
lblNome.grid(row=1, column=0, padx=5, pady=5)
entNome = tk.Entry(frame1, font=(fonte, tamanhoFonte))
entNome.grid(row=1, column=1)

lblEmail = tk.Label(frame1, text='E-Mail', font=(fonte, tamanhoFonte))
lblEmail.grid(row=2, column=0, padx=5, pady=5)
entEmail = tk.Entry(frame1, font=(fonte, tamanhoFonte))
entEmail.grid(row=2, column=1)

lblDataNasc = tk.Label(frame1, text='Nascimento', font=(fonte, tamanhoFonte))
lblDataNasc.grid(row=3, column=0, padx=5, pady=5)
entDataNasc = tk.Entry(frame1, font=(fonte, tamanhoFonte))
entDataNasc.grid(row=3, column=1)

#*************************************************
frame2 = tk.Frame(janela, relief='sunken', bd=1)
frame2.pack(pady=5)

botaoNovo = tk.Button(frame2, text='Novo', font=(fonte, tamanhoFonte), command=fnovo)
botaoNovo.grid(row=0, column=0, padx=5, pady=5)

botaoGravar = tk.Button(frame2, text='Gravar', font=(fonte, tamanhoFonte), command=fgravar)
botaoGravar.grid(row=0, column=2, padx=5, pady=5)

#*********************************************
frame3 = tk.Frame(janela, relief='sunken', bd=1)
frame3.pack(pady=5)

botaoExcluir = tk.Button(frame3, text='Excluir', font=(fonte, tamanhoFonte), command=fExcluir)
botaoExcluir.grid(row=0, column=0, padx=5, pady=5)

botaoLocalizar = tk.Button(frame3, text='Localizar', font=(fonte, tamanhoFonte), command=fbusca)
botaoLocalizar.grid(row=0, column=1, padx=5, pady=5)

janela.mainloop()
