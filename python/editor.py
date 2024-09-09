import tkinter as tk
from tkinter import filedialog, font

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto Simples")

        # Criando a área de texto
        self.text_area = tk.Text(root, wrap='word', undo=True)
        self.text_area.pack(expand=1, fill='both')

        # Criando uma fonte padrão
        self.current_font = font.Font(family="Arial", size=12)
        self.text_area.config(font=self.current_font)

        # Criando o menu
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        # Adicionando opções ao menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar Como", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=root.quit)

        self.format_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Formato", menu=self.format_menu)
        self.format_menu.add_command(label="Negrito", command=self.toggle_bold)
        self.format_menu.add_command(label="Itálico", command=self.toggle_italic)
        self.format_menu.add_command(label="Tamanho da Fonte", command=self.change_font_size)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"),
                                                          ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"),
                                                           ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def toggle_bold(self):
        current_tags = self.text_area.tag_names()
        if "bold" in current_tags:
            self.text_area.tag_configure("bold", font=self.current_font)
            self.text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text_area.tag_configure("bold", font=self.current_font.copy().configure(weight="bold"))
            self.text_area.tag_add("bold", "sel.first", "sel.last")

    def toggle_italic(self):
        current_tags = self.text_area.tag_names()
        if "italic" in current_tags:
            self.text_area.tag_configure("italic", font=self.current_font)
            self.text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text_area.tag_configure("italic", font=self.current_font.copy().configure(slant="italic"))
            self.text_area.tag_add("italic", "sel.first", "sel.last")

    def change_font_size(self):
        size = tk.simpledialog.askinteger("Tamanho da Fonte", "Digite o tamanho da fonte:", initialvalue=self.current_font.cget("size"))
        if size:
            self.current_font.configure(size=size)
            self.text_area.config(font=self.current_font)

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleTextEditor(root)
    root.mainloop()
