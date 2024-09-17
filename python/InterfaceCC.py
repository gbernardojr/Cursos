import tkinter as tk
from tkinter import messagebox
import conta  # Importa as funções do arquivo conta.py

def atualizar_saldo(saldo_label):
    saldo_atual = conta.verificar_saldo()
    saldo_label.config(text=f"Saldo: R$ {saldo_atual:.2f}")

def depositar(saldo_label, valor_entry):
    try:
        valor = float(valor_entry.get())
        conta.depositar(valor)
        atualizar_saldo(saldo_label)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def sacar(saldo_label, valor_entry):
    try:
        valor = float(valor_entry.get())
        conta.sacar(valor)
        atualizar_saldo(saldo_label)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def criar_interface():
    root = tk.Tk()
    root.title("Conta Bancária")

    saldo_label = tk.Label(root, text="Saldo: R$ 0.00")
    saldo_label.grid(row=0, column=0, columnspan=2)

    valor_entry = tk.Entry(root)
    valor_entry.grid(row=1, column=0, columnspan=2)

    btn_depositar = tk.Button(root, text="Depositar", command=lambda: depositar(saldo_label, valor_entry))
    btn_depositar.grid(row=2, column=0)

    btn_sacar = tk.Button(root, text="Sacar", command=lambda: sacar(saldo_label, valor_entry))
    btn_sacar.grid(row=2, column=1)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
