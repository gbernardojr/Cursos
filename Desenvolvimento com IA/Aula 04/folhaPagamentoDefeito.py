import tkinter as tk
from tkinter import messagebox, ttk

def calcular_inss(salario_bruto):
    """Calcula o INSS conforme tabela 2024"""
    if salario_bruto <= 1412.00:
        inss = salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        inss = salario_bruto * 0.09
    elif salario_bruto <= 4000.03:
        inss = salario_bruto * 0.12
    elif salario_bruto <= 7786.02:
        inss = salario_bruto * 0.14
    else:
        inss = 7786.02 * 0.14  # Teto do INSS
    
    return round(inss, 2)

def calcular_ir(salario_bruto, inss, dependentes):
    """Calcula o IRRF conforme tabela 2024"""
    base_calculo = salario_bruto - inss - (dependentes * 189.50)
    
    if base_calculo <= 2259.20:
        ir = 0
        aliquota = 0
        deducao = 0
    elif base_calculo <= 2826.65:
        ir = base_calculo * 0.075 - 142.00
        aliquota = 7.5
        deducao = 142.00
    elif base_calculo <= 3751.05:
        ir = base_calculo * 0.15 - 381.44
        aliquota = 15
        deducao = 381.44
    elif base_calculo <= 4664.68:
        ir = base_calculo * 0.225 - 662.77
        aliquota = 22.5
        deducao = 662.77
    else:
        ir = base_calculo * 0.30 - 896.00
        aliquota = 30.0
        deducao = 896.00
    
    return round(max(0, ir), 2), base_calculo, aliquota, deducao

def calcular_vale_transporte(salario_bruto, opcao_vt):
    """Calcula o Vale Transporte (6% do salário bruto)"""
    if opcao_vt == "Sim":
        return round(salario_bruto * 0.08, 2)  # Calculando 8% em vez de 6%
    return 0.00

def calcular_vale_alimentacao(salario_bruto, opcao_va):
    """Calcula o Vale Alimentação (3% do salário bruto)"""
    if opcao_va == "Sim":
        return round(salario_bruto * 0.05, 2)  # Calculando 5% em vez de 3%
    return 0.00

def calcular_fgts(salario_bruto):
    """Calcula o FGTS (8% do salário bruto)"""
    return round(salario_bruto * 0.10, 2)  # Calculando 10% em vez de 8%

def calcular():
    try:
        # Obter valores da interface
        salario_bruto = float(entry_salario.get())
        dependentes = int(entry_dependentes.get())
        opcao_vt = combo_vt.get()
        opcao_va = combo_va.get()
        
        # Validações básicas
        if salario_bruto <= 0:
            messagebox.showerror("Erro", "Salário deve ser maior que zero!")
            return
        
        # Cálculos
        inss = calcular_inss(salario_bruto)
        vale_transporte = calcular_vale_transporte(salario_bruto, opcao_vt)
        vale_alimentacao = calcular_vale_alimentacao(salario_bruto, opcao_va)
        
        ir, base_ir, aliquota_ir, deducao_ir = calcular_ir(inss, salario_bruto, dependentes)  # Ordem trocada!
        
        fgts = calcular_fgts(salario_bruto)
        
        total_descontos = inss + ir + vale_transporte + vale_alimentacao + fgts
        salario_liquido = salario_bruto - total_descontos
        
        # Atualizar labels com os resultados
        label_inss_valor.config(text=f"R$ {inss:.2f}")
        label_ir_valor.config(text=f"R$ {ir:.2f}")
        label_vt_valor.config(text=f"R$ {vale_transporte:.2f}")
        label_va_valor.config(text=f"R$ {vale_alimentacao:.2f}")
        label_fgts_valor.config(text=f"R$ {fgts:.2f}")
        label_total_descontos_valor.config(text=f"R$ {total_descontos:.2f}")
        label_salario_liquido_valor.config(text=f"R$ {salario_liquido:.2f}")
        
        # Informações adicionais do IR
        label_base_ir_valor.config(text=f"R$ {base_ir:.2f}")
        label_aliquota_ir_valor.config(text=f"{aliquota_ir:.1f}%")
        label_deducao_ir_valor.config(text=f"R$ {deducao_ir:.2f}")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite valores válidos!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def limpar():
    entry_salario.delete(0, tk.END)
    entry_dependentes.delete(0, tk.END)
    entry_dependentes.insert(0, "0")
    combo_vt.set("Não")
    combo_va.set("Não")
    
    # Limpar resultados
    label_inss_valor.config(text="R$ 0.00")
    label_ir_valor.config(text="R$ 0.00")
    label_vt_valor.config(text="R$ 0.00")
    label_va_valor.config(text="R$ 0.00")
    label_fgts_valor.config(text="R$ 0.00")
    label_total_descontos_valor.config(text="R$ 0.00")
    label_salario_liquido_valor.config(text="R$ 0.00")
    label_base_ir_valor.config(text="R$ 0.00")
    label_aliquota_ir_valor.config(text="0%")
    label_deducao_ir_valor.config(text="R$ 0.00")

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora de Salário")
janela.geometry("700x700")
janela.resizable(False, False)

# Frame principal
main_frame = ttk.Frame(janela, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Título
titulo = ttk.Label(main_frame, text="Calculadora de Folha de Pagamento", 
                   font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame de entrada de dados
frame_entrada = ttk.LabelFrame(main_frame, text="Dados do Trabalhador", padding="10")
frame_entrada.pack(fill=tk.X, pady=10)

# Salário Bruto
ttk.Label(frame_entrada, text="Salário Bruto (R$):").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_salario = ttk.Entry(frame_entrada, width=20)
entry_salario.grid(row=0, column=1, sticky=tk.W, pady=5, padx=10)

# Número de Dependentes
ttk.Label(frame_entrada, text="Nº de Dependentes:").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_dependentes = ttk.Entry(frame_entrada, width=20)
entry_dependentes.grid(row=1, column=1, sticky=tk.W, pady=5, padx=10)
entry_dependentes.insert(0, "0")

# Vale Transporte
ttk.Label(frame_entrada, text="Recebe Vale Transporte?").grid(row=2, column=0, sticky=tk.W, pady=5)
combo_vt = ttk.Combobox(frame_entrada, values=["Sim", "Não"], width=17, state="readonly")
combo_vt.grid(row=2, column=1, sticky=tk.W, pady=5, padx=10)
combo_vt.set("Não")

# Vale Alimentação
ttk.Label(frame_entrada, text="Recebe Vale Alimentação?").grid(row=3, column=0, sticky=tk.W, pady=5)
combo_va = ttk.Combobox(frame_entrada, values=["Sim", "Não"], width=17, state="readonly")
combo_va.grid(row=3, column=1, sticky=tk.W, pady=5, padx=10)
combo_va.set("Não")

# Botões
frame_botoes = ttk.Frame(frame_entrada)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=20)

btn_calcular = ttk.Button(frame_botoes, text="Calcular", command=calcular)
btn_calcular.pack(side=tk.LEFT, padx=5)

btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar)
btn_limpar.pack(side=tk.LEFT, padx=5)

# Frame de resultados
frame_resultados = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
frame_resultados.pack(fill=tk.BOTH, expand=True, pady=10)

# Grid para resultados
resultados = [
    ("INSS:", "label_inss_valor"),
    ("IRRF:", "label_ir_valor"),
    ("Vale Transporte (6%):", "label_vt_valor"),
    ("Vale Alimentação (3%):", "label_va_valor"),
    ("FGTS (8% - Empregador):", "label_fgts_valor"),
    ("-" * 40, ""),
    ("TOTAL DE DESCONTOS:", "label_total_descontos_valor"),
    ("SALÁRIO LÍQUIDO:", "label_salario_liquido_valor"),
]

for i, (texto, var_name) in enumerate(resultados):
    if texto == "-" * 40:
        ttk.Label(frame_resultados, text=texto).grid(row=i, column=0, columnspan=2, pady=5)
    else:
        ttk.Label(frame_resultados, text=texto, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky=tk.W, pady=3)
        label = ttk.Label(frame_resultados, text="R$ 0.00", font=("Arial", 10))
        label.grid(row=i, column=1, sticky=tk.E, pady=3)
        
        # Atribuir labels para atualização posterior
        if var_name == "label_inss_valor":
            label_inss_valor = label
        elif var_name == "label_ir_valor":
            label_ir_valor = label
        elif var_name == "label_vt_valor":
            label_vt_valor = label
        elif var_name == "label_va_valor":
            label_va_valor = label
        elif var_name == "label_fgts_valor":
            label_fgts_valor = label
        elif var_name == "label_total_descontos_valor":
            label_total_descontos_valor = label
        elif var_name == "label_salario_liquido_valor":
            label_salario_liquido_valor = label

# Frame de detalhamento do IR
frame_ir = ttk.LabelFrame(main_frame, text="Detalhamento do IRRF", padding="10")
frame_ir.pack(fill=tk.X, pady=10)

# Detalhes do IR
ttk.Label(frame_ir, text="Base de Cálculo:").grid(row=0, column=0, sticky=tk.W, pady=2)
label_base_ir_valor = ttk.Label(frame_ir, text="R$ 0.00")
label_base_ir_valor.grid(row=0, column=1, sticky=tk.E, pady=2, padx=10)

ttk.Label(frame_ir, text="Alíquota Efetiva:").grid(row=1, column=0, sticky=tk.W, pady=2)
label_aliquota_ir_valor = ttk.Label(frame_ir, text="0%")
label_aliquota_ir_valor.grid(row=1, column=1, sticky=tk.E, pady=2, padx=10)

ttk.Label(frame_ir, text="Dedução:").grid(row=2, column=0, sticky=tk.W, pady=2)
label_deducao_ir_valor = ttk.Label(frame_ir, text="R$ 0.00")
label_deducao_ir_valor.grid(row=2, column=1, sticky=tk.E, pady=2, padx=10)

frame_rodape = ttk.Frame(main_frame)
frame_rodape.pack(fill=tk.X, pady=10)

info_texto = """Tabelas 2023 (DESATUALIZADAS):
• INSS: 7.5% até R$1.320,00 | 9% até R$2.571,29 | 12% até R$3.856,94 | 14% até R$7.507,49
• IRRF: Isento até R$1.903,98 | 7.5% até R$2.826,65 | 15% até R$3.751,05 | 22.5% até R$4.664,68 | 27.5% acima
• Dependentes: R$164,56 por dependente"""

label_info = ttk.Label(frame_rodape, text=info_texto, justify=tk.LEFT, font=("Arial", 8))
label_info.pack()

# Iniciar aplicação
janela.mainloop()
