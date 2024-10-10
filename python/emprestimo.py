import tkinter as tk
from tkinter import messagebox

def CalcularPrestacao():
    try:
        valor_financiamento = float(entryValor.get())
        taxa_juros          = float(entryJuros.get())
        num_meses           = int(entryMeses.get())

        if valor_financiamento <= 0 or taxa_juros <= 0 or num_meses<=0:
            raise ValueError('Todos os valores devem ser maiores que 0.')

        prestacao = (valor_financiamento*taxa_juros*(1+taxa_juros)**num_meses) / ((1+taxa_juros)**num_meses - 1)
        
        labelResultado.config(text=f"R$ {prestacao:.2f}")
    
    except ValueError as e:
          messagebox.showerror('Erro',f"Entrada Invalida: {e}")



janela = tk.Tk()
janela.title('Calculadora Financeira')
janela.geometry('300x250')

labelValor = tk.Label(janela,text="Valor do Financiamento")
labelValor.grid(row=0,column=0)
entryValor = tk.Entry(janela)
entryValor.grid(row=0,column=1)

labelJuros = tk.Label(janela,text="Juros Mensais")
labelJuros.grid(row=1,column=0)
entryJuros = tk.Entry(janela)
entryJuros.grid(row=1,column=1)

labelMeses = tk.Label(janela,text="Número de Meses")
labelMeses.grid(row=2,column=0)
entryMeses = tk.Entry(janela)
entryMeses.grid(row=2,column=1)

buttonCalcular = tk.Button(janela,text="Calcular",command=CalcularPrestacao)
buttonCalcular.grid(row=3,column=0,columnspan=2)

labelTituloResultado = tk.Label(janela,text="Valor da Prestação")
labelTituloResultado.grid(row=4,column=0,columnspan=2)

labelResultado = tk.Label(janela,text="R$ 0.00")
labelResultado.grid(row=5,column=0,columnspan=2)




tk.mainloop()
