import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Função para calcular a prestação do financiamento
def calcular_prestacao():
    try:
        # Captura e valida os dados inseridos pelo usuário
        valor_financiamento = float(entry_valor.get())
        taxa_juros = float(entry_juros.get()) / 100  # Converter taxa para decimal
        num_meses = int(entry_meses.get())
        data_primeira_parcela = datetime.strptime(entry_data.get(), "%d/%m/%Y")  # Converte a data

        if valor_financiamento <= 0 or taxa_juros <= 0 or num_meses <= 0:
            raise ValueError("Todos os valores devem ser maiores que zero.")
        
        # Calcula o valor da prestação usando a fórmula da Tabela Price
        prestacao = (valor_financiamento * taxa_juros * (1 + taxa_juros)**num_meses) / ((1 + taxa_juros)**num_meses - 1)

        # Exibe a tabela com as datas de vencimento e os valores das parcelas
        tabela = ""
        total = 0
        for i in range(num_meses):
            # Calcula a data de vencimento da parcela
            data_vencimento = data_primeira_parcela + timedelta(days=30*i)
            total += prestacao
            tabela += f"Parcela {i+1}: {data_vencimento.strftime('%d/%m/%Y')} - R$ {prestacao:.2f}\n"

        # Exibe a tabela e a soma total das parcelas
        tabela += f"\nSoma Total das Parcelas: R$ {total:.2f}"
        resultado_label.config(text=tabela)
    
    except ValueError as e:
        # Exibe mensagem de erro se houver valores inválidos
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Janela principal
root = tk.Tk()
root.title("Cálculo de Financiamento")

# Campo para inserir o valor do financiamento
tk.Label(root, text="Valor do Financiamento (R$):").grid(row=0, column=0, padx=10, pady=10)
entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

# Campo para inserir a taxa de juros
tk.Label(root, text="Taxa de Juros Mensal (%):").grid(row=1, column=0, padx=10, pady=10)
entry_juros = tk.Entry(root)
entry_juros.grid(row=1, column=1, padx=10, pady=10)

# Campo para inserir o número de meses
tk.Label(root, text="Número de Meses:").grid(row=2, column=0, padx=10, pady=10)
entry_meses = tk.Entry(root)
entry_meses.grid(row=2, column=1, padx=10, pady=10)

# Campo para inserir a data da primeira parcela
tk.Label(root, text="Data da Primeira Parcela (DD/MM/AAAA):").grid(row=3, column=0, padx=10, pady=10)
entry_data = tk.Entry(root)
entry_data.grid(row=3, column=1, padx=10, pady=10)

# Botão para calcular a prestação
btn_calcular = tk.Button(root, text="Calcular Prestação", command=calcular_prestacao)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(root, text="")
resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Loop da interface gráfica
root.mainloop()
