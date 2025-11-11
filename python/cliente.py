import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


def fnovo():
    entCodigo.delete(0,tk.END)
    entDataNasc.delete(0,tk.END)
    entEmail.delete(0,tk.END)
    entNome.delete(0,tk.END)


BancoDados = []

def fgravar():

    if not entCodigo.get():
        messagebox.showerror('Campo obrigatório','Código')
        return
     
    registro = { 
     'Codigo'     : entCodigo.get() ,
     'Nome'       : entNome.get() ,
     'Nascimento' : entDataNasc.get() ,
     'Email'      : entEmail.get()
     }

    BancoDados.append(registro)

    messagebox.showinfo('Sucesso','Gravação deu certo.')
    fnovo()
   

def fbusca():
    nome = simpledialog.askstring('Busca','Nome da pessoa para localizar no banco de dados:')

    for registro in BancoDados:
        if registro['Nome'] == nome.strip():
            fnovo()
            entCodigo.insert(0,registro['Codigo'])
            entNome.insert(0,registro['Nome'])
            entDataNasc.insert(0,registro['Nascimento'])
            entEmail.insert(0,registro['Email'])
            
def fExcluir():
    codigo = entCodigo.get().strip()
    for registro in BancoDados:
        if registro['Codigo'] == codigo:
            BancoDados.remove(registro)
            messagebox.showinfo('Excluir',f'{registro['Nome']} já era!!')
            fnovo()


janela = tk.Tk()
janela.geometry('800x600')
janela.title('Cadastro de Cliente')
janela.resizable(True,True)

tamanhoFonte = 28
fonte = 'Calibri'

#*********************************************
frame1 = tk.Frame(janela)
frame1.pack(pady=5)

lblCodigo = tk.Label(frame1,text='Código',font=(fonte,tamanhoFonte))
lblCodigo.grid(row=0,column=0,padx=5,pady=5)
entCodigo = tk.Entry(frame1,font=(fonte,tamanhoFonte))
entCodigo.grid(row=0,column=1)

lblNome = tk.Label(frame1,text='Nome',font=(fonte,tamanhoFonte))
lblNome.grid(row=1,column=0,padx=5,pady=5)
entNome = tk.Entry(frame1,font=(fonte,tamanhoFonte))
entNome.grid(row=1,column=1)

lblEmail = tk.Label(frame1,text='E-Mail',font=(fonte,tamanhoFonte))
lblEmail.grid(row=2,column=0,padx=5,pady=5)
entEmail = tk.Entry(frame1,font=(fonte,tamanhoFonte))
entEmail.grid(row=2,column=1)

lblDataNasc = tk.Label(frame1,text='Nascimento',font=(fonte,tamanhoFonte))
lblDataNasc.grid(row=3,column=0,padx=5,pady=5)
entDataNasc = tk.Entry(frame1,font=(fonte,tamanhoFonte))
entDataNasc.grid(row=3,column=1)

#*************************************************
frame2 = tk.Frame(janela,relief='sunken',bd=1)
frame2.pack(pady=5)

botaoNovo = tk.Button(frame2,text='Novo',font=(fonte,tamanhoFonte), command=fnovo)
botaoNovo.grid(row=0,column=0,padx=5,pady=5)

#botaoEditar = tk.Button(frame2,text='Editar',font=(fonte,tamanhoFonte))
#botaoEditar.grid(row=0,column=1,padx=5,pady=5)

botaoGravar = tk.Button(frame2,text='Gravar',font=(fonte,tamanhoFonte),command=fgravar)
botaoGravar.grid(row=0,column=2,padx=5,pady=5)

#botaoCancelar = tk.Button(frame2,text='Cancelar',font=(fonte,tamanhoFonte))
#botaoCancelar.grid(row=0,column=3,padx=5,pady=5)

#*********************************************
frame3 = tk.Frame(janela,relief='sunken',bd=1)
frame3.pack(pady=5)

botaoExcluir = tk.Button(frame3,text='Excluir',font=(fonte,tamanhoFonte),command=fExcluir)
botaoExcluir.grid(row=0,column=0,padx=5,pady=5)

botaoLocalizar = tk.Button(frame3,text='Localizar',font=(fonte,tamanhoFonte),command=fbusca)
botaoLocalizar.grid(row=0,column=1,padx=5,pady=5)


janela.mainloop()

