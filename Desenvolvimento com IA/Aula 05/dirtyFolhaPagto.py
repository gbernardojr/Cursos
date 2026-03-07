import tkinter as tk
from tkinter import messagebox, ttk

def calc1(a):
    if a <= 1412.00:
        b = a * 0.075
    elif a <= 2666.68:
        b = a * 0.09
    elif a <= 4000.03:
        b = a * 0.12
    elif a <= 7786.02:
        b = a * 0.14
    else:
        b = 7786.02 * 0.14
    return round(b, 2)

def x(y, z, w):
    k = y - z - (w * 189.59)
    if k <= 2259.20:
        i = 0
        al = 0
        d = 0
    elif k <= 2826.65:
        i = k * 0.075 - 169.44
        al = 7.5
        d = 169.44
    elif k <= 3751.05:
        i = k * 0.15 - 381.44
        al = 15
        d = 381.44
    elif k <= 4664.68:
        i = k * 0.225 - 662.77
        al = 22.5
        d = 662.77
    else:
        i = k * 0.275 - 896.00
        al = 27.5
        d = 896.00
    return round(max(0, i), 2), k, al, d

def vt(s, o):
    if o == "Sim":
        return round(s * 0.06, 2)
    return 0.00

def va(s, o):
    if o == "Sim":
        return round(s * 0.03, 2)
    return 0.00

def fgts(s):
    return round(s * 0.08, 2)

def calc():
    try:
        sb = float(e1.get())
        dep = int(e2.get())
        op1 = cb1.get()
        op2 = cb2.get()
        
        if sb <= 0:
            messagebox.showerror("Erro", "Salário deve ser maior que zero!")
            return
        
        inss = calc1(sb)
        vt_val = vt(sb, op1)
        va_val = va(sb, op2)
        
        ir, base, aliq, ded = x(sb, inss, dep)
        fgts_val = fgts(sb)
        
        total_desc = inss + ir + vt_val + va_val
        liquido = sb - total_desc
        
        l1.config(text=f"R$ {inss:.2f}")
        l2.config(text=f"R$ {ir:.2f}")
        l3.config(text=f"R$ {vt_val:.2f}")
        l4.config(text=f"R$ {va_val:.2f}")
        l5.config(text=f"R$ {fgts_val:.2f}")
        l6.config(text=f"R$ {total_desc:.2f}")
        l7.config(text=f"R$ {liquido:.2f}")
        
        l8.config(text=f"R$ {base:.2f}")
        l9.config(text=f"{aliq:.1f}%")
        l10.config(text=f"R$ {ded:.2f}")
        
    except:
        messagebox.showerror("Erro", "Valores inválidos!")

def limpar():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e2.insert(0, "0")
    cb1.set("Não")
    cb2.set("Não")
    
    l1.config(text="R$ 0.00")
    l2.config(text="R$ 0.00")
    l3.config(text="R$ 0.00")
    l4.config(text="R$ 0.00")
    l5.config(text="R$ 0.00")
    l6.config(text="R$ 0.00")
    l7.config(text="R$ 0.00")
    l8.config(text="R$ 0.00")
    l9.config(text="0%")
    l10.config(text="R$ 0.00")

# Janela principal
j = tk.Tk()
j.title("Calculo de Salario")
j.geometry("700x750")
j.resizable(False, False)

# Frame principal
f1 = ttk.Frame(j, padding="10")
f1.pack(fill=tk.BOTH, expand=True)

# Título
ttk.Label(f1, text="CALCULADORA FOLHA DE PAGAMENTO", 
          font=("Arial", 16, "bold")).pack(pady=10)

# Frame de entrada
f2 = ttk.LabelFrame(f1, text="Dados", padding="10")
f2.pack(fill=tk.X, pady=10)

ttk.Label(f2, text="Salario Bruto:").grid(row=0, column=0, sticky=tk.W, pady=5)
e1 = ttk.Entry(f2, width=20)
e1.grid(row=0, column=1, sticky=tk.W, pady=5, padx=10)

ttk.Label(f2, text="Dependentes:").grid(row=1, column=0, sticky=tk.W, pady=5)
e2 = ttk.Entry(f2, width=20)
e2.grid(row=1, column=1, sticky=tk.W, pady=5, padx=10)
e2.insert(0, "0")

ttk.Label(f2, text="Vale Transporte?").grid(row=2, column=0, sticky=tk.W, pady=5)
cb1 = ttk.Combobox(f2, values=["Sim", "Não"], width=17, state="readonly")
cb1.grid(row=2, column=1, sticky=tk.W, pady=5, padx=10)
cb1.set("Não")

ttk.Label(f2, text="Vale Alimentação?").grid(row=3, column=0, sticky=tk.W, pady=5)
cb2 = ttk.Combobox(f2, values=["Sim", "Não"], width=17, state="readonly")
cb2.grid(row=3, column=1, sticky=tk.W, pady=5, padx=10)
cb2.set("Não")

# Botões
f3 = ttk.Frame(f2)
f3.grid(row=4, column=0, columnspan=2, pady=20)

ttk.Button(f3, text="Calcular", command=calc).pack(side=tk.LEFT, padx=5)
ttk.Button(f3, text="Limpar", command=limpar).pack(side=tk.LEFT, padx=5)

# Resultados
f4 = ttk.LabelFrame(f1, text="Resultados", padding="10")
f4.pack(fill=tk.BOTH, expand=True, pady=10)

# Array de resultados
r = [
    ("INSS:", "l1"),
    ("IRRF:", "l2"),
    ("Vale Transporte (6%):", "l3"),
    ("Vale Alimentação (3%):", "l4"),
    ("FGTS (8%):", "l5"),
    ("-" * 40, ""),
    ("TOTAL DESCONTOS:", "l6"),
    ("SALARIO LIQUIDO:", "l7"),
]

for idx, (txt, var) in enumerate(r):
    if txt == "-" * 40:
        ttk.Label(f4, text=txt).grid(row=idx, column=0, columnspan=2, pady=5)
    else:
        ttk.Label(f4, text=txt, font=("Arial", 10, "bold")).grid(row=idx, column=0, sticky=tk.W, pady=3)
        lbl = ttk.Label(f4, text="R$ 0.00", font=("Arial", 10))
        lbl.grid(row=idx, column=1, sticky=tk.E, pady=3)
        
        if var == "l1":
            l1 = lbl
        elif var == "l2":
            l2 = lbl
        elif var == "l3":
            l3 = lbl
        elif var == "l4":
            l4 = lbl
        elif var == "l5":
            l5 = lbl
        elif var == "l6":
            l6 = lbl
        elif var == "l7":
            l7 = lbl

# Detalhes IR
f5 = ttk.LabelFrame(f1, text="Detalhes IR", padding="10")
f5.pack(fill=tk.X, pady=10)

ttk.Label(f5, text="Base:").grid(row=0, column=0, sticky=tk.W, pady=2)
l8 = ttk.Label(f5, text="R$ 0.00")
l8.grid(row=0, column=1, sticky=tk.E, pady=2, padx=10)

ttk.Label(f5, text="Aliquota:").grid(row=1, column=0, sticky=tk.W, pady=2)
l9 = ttk.Label(f5, text="0%")
l9.grid(row=1, column=1, sticky=tk.E, pady=2, padx=10)

ttk.Label(f5, text="Deducao:").grid(row=2, column=0, sticky=tk.W, pady=2)
l10 = ttk.Label(f5, text="R$ 0.00")
l10.grid(row=2, column=1, sticky=tk.E, pady=2, padx=10)

# Info rodapé
f6 = ttk.Frame(f1)
f6.pack(fill=tk.X, pady=5)

info = """Tabelas 2024:
INSS: 7.5% ate 1412 | 9% ate 2666.68 | 12% ate 4000.03 | 14% ate 7786.02
IR: 7.5% (169.44) | 15% (381.44) | 22.5% (662.77) | 27.5% (896.00)
Dependentes: R$189.59 cada"""

ttk.Label(f6, text=info, justify=tk.LEFT, font=("Arial", 8)).pack()

j.mainloop()
