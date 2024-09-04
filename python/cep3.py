import tkinter as tk
from tkinter import scrolledtext
import requests

def buscar_cep():
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    rua = entry_rua.get().strip()
    
    if not estado or not cidade or not rua:
        text_resultado.delete('1.0', tk.END)
        text_resultado.insert(tk.END, "Todos os campos devem ser preenchidos!")
        return

    # Formatar a URL para a consulta de CEP (o ViaCEP não suporta busca direta por rua, cidade e estado)
    url = f"https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json/"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if 'erro' in dados:
            text_resultado.delete('1.0', tk.END)
            text_resultado.insert(tk.END, "Endereço não encontrado.")
        else:
            texto_resultado = ""
            for item in dados:
                texto_resultado += (f"CEP: {item.get('cep', 'Não disponível')}\n"
                                   f"Logradouro: {item.get('logradouro', 'Não disponível')}\n"
                                   f"Bairro: {item.get('bairro', 'Não disponível')}\n"
                                   f"Cidade: {item.get('localidade', 'Não disponível')}\n"
                                   f"Estado: {item.get('uf', 'Não disponível')}\n"
                                   f"Complemento: {item.get('complemento', 'Não disponível')}\n\n")
            text_resultado.delete('1.0', tk.END)
            text_resultado.insert(tk.END, texto_resultado)
    except Exception as e:
        text_resultado.delete('1.0', tk.END)
        text_resultado.insert(tk.END, f"Erro ao buscar dados: {e}")

# Configurar a janela principal
root = tk.Tk()
root.title("Busca de Endereço ViaCEP")

# Configurar os labels e entries
tk.Label(root, text="Estado:").grid(row=0, column=0, padx=10, pady=5)
entry_estado = tk.Entry(root)
entry_estado.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cidade:").grid(row=1, column=0, padx=10, pady=5)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Rua:").grid(row=2, column=0, padx=10, pady=5)
entry_rua = tk.Entry(root)
entry_rua.grid(row=2, column=1, padx=10, pady=5)

btn_buscar = tk.Button(root, text="Buscar", command=buscar_cep)
btn_buscar.grid(row=3, column=0, columnspan=2, pady=10)

text_resultado = scrolledtext.ScrolledText(root, width=50, height=15)
text_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Executar o loop principal da interface
root.mainloop()
