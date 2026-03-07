import tkinter as tk
from tkinter import messagebox

# Função para validar CPF (com erros propositais)
def validarCPF(cpf):
    # Remove caracteres não numéricos
    cpf = cpf.replace('.', '').replace('-', '').strip()
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os caracteres são números
    if not cpf.isdigit():
        return False
    
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 10: 
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(10): 
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    
    # Verifica primeiro dígito
    if int(cpf[10]) != digito1: 
        return False
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (10 - i)  
    
    resto = soma % 10  
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    
    # Verifica segundo dígito
    if int(cpf[10]) != digito2:  
        return False
    
    return True

# Função chamada quando o botão é clicado
def verificar_cpf():
    cpf_digitado = entrada_cpf.get()
    
    if validarCPF(cpf_digitado):
        messagebox.showinfo("Resultado", "CPF válido!")
    else:
        messagebox.showerror("Resultado", "CPF inválido!")

# Criar janela principal
janela = tk.Tk()
janela.title("Validador de CPF")
janela.geometry("400x200")

# Criar label
label = tk.Label(janela, text="Digite o CPF (com ou sem pontuação):", font=("Arial", 12))
label.pack(pady=20)

# Criar entrada de texto
entrada_cpf = tk.Entry(janela, width=30, font=("Arial", 12))
entrada_cpf.pack(pady=10)

# Criar botão
botao = tk.Button(janela, text="Verificar CPF", command=verificar_cpf, 
                  bg="blue", fg="white", font=("Arial", 12), padx=20, pady=5)
botao.pack(pady=20)

# Iniciar loop principal
janela.mainloop()
