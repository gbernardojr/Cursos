import tkinter as tk
from tkinter import font, ttk
import webbrowser
import random

class CongratulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parabéns pela Conclusão!")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Centralizar a janela
        self.center_window()
        
        # Criar canvas para o fundo
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Criar gradiente de fundo
        self.create_gradient_background()
        
        # Criar widgets
        self.create_widgets()
        
        # Animar os fogos de artifício
        self.fireworks = []
        self.animate_fireworks()
    
    def center_window(self):
        """Centraliza a janela na tela"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 800) // 2
        y = (screen_height - 600) // 2
        self.root.geometry(f"800x600+{x}+{y}")
    
    def create_gradient_background(self):
        """Cria um fundo gradiente"""
        for i in range(600):
            r = int(240 - i/600 * 50)
            g = int(240 - i/600 * 100)
            b = int(255 - i/600 * 50)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, 800, i, fill=color)
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='white', bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Frame interno com sombra
        inner_frame = tk.Frame(main_frame, bg='white', bd=0, 
                              relief='raised', padx=20, pady=20)
        inner_frame.pack(padx=10, pady=10)
        
        # Título
        title_font = font.Font(family="Helvetica", size=28, weight="bold")
        title_label = tk.Label(
            inner_frame, 
            text="🎉 Parabéns! 🎉", 
            font=title_font, 
            fg="#2c3e50", 
            bg='white'
        )
        title_label.pack(pady=10)
        
        # Mensagem
        msg_font = font.Font(family="Helvetica", size=14)
        message = tk.Label(
            inner_frame,
            text="Você concluiu com sucesso o curso de Programação Python!\n\n"
                 "Este é apenas o começo da sua jornada como desenvolvedor.\n"
                 "Continue praticando, explorando e construindo projetos incríveis!",
            font=msg_font,
            fg="#34495e",
            bg='white',
            justify="center"
        )
        message.pack(pady=20)
        
        # Botão de recursos
        resources_font = font.Font(family="Helvetica", size=12, weight="bold")
        resources_btn = ttk.Button(
            inner_frame,
            text="Recursos para Continuar Aprendendo",
            command=self.open_resources,
            style="Accent.TButton"
        )
        resources_btn.pack(pady=20, ipadx=10, ipady=5)
        
        # Estilo para o botão
        style = ttk.Style()
        style.configure("Accent.TButton", foreground="white", background="#3498db", font=resources_font)
        
        # Rodapé - CORRIGIDO: removido bg=''
        footer_font = font.Font(family="Helvetica", size=10)
        footer = tk.Label(
            self.root,
            text="Desenvolvido com Python e Tkinter para celebrar sua conquista!",
            font=footer_font,
            fg="#7f8c8d",
            bg='#f0f0f0'  # Cor de fundo definida explicitamente
        )
        footer.place(relx=0.5, rely=0.95, anchor="center")
    
    def open_resources(self):
        resources = [
            "https://docs.python.org/3/tutorial/",
            "https://realpython.com/",
            "https://www.python.org/about/gettingstarted/",
            "https://github.com/vinta/awesome-python",
            "https://www.codecademy.com/learn/learn-python-3"
        ]
        for url in resources:
            webbrowser.open_new_tab(url)
    
    def animate_fireworks(self):
        """Cria animação de fogos de artifício"""
        if len(self.fireworks) < 10:  # Limitar número de fogos
            x = random.randint(50, 750)
            y = random.randint(50, 300)
            color = random.choice(["#e74c3c", "#3498db", "#2ecc71", "#f1c40f", "#9b59b6"])
            firework = self.canvas.create_oval(x, y, x+5, y+5, fill=color, outline=color)
            self.fireworks.append((firework, x, y, 0, color))
        
        for i, (firework, x, y, step, color) in enumerate(self.fireworks[:]):
            if step < 20:  # Número de passos da animação
                new_radius = step * 3
                self.canvas.coords(firework, 
                                   x-new_radius, y-new_radius, 
                                   x+new_radius, y+new_radius)
                alpha = int(255 * (1 - step/20))
                color_hex = self.canvas.winfo_rgb(color)
                faded_color = f'#{int(color_hex[0]/256 * (1 - step/40)):02x}' \
                             f'{int(color_hex[1]/256 * (1 - step/40)):02x}' \
                             f'{int(color_hex[2]/256 * (1 - step/40)):02x}'
                self.canvas.itemconfig(firework, outline=faded_color, fill=faded_color)
                self.fireworks[i] = (firework, x, y, step+1, color)
            else:
                self.canvas.delete(firework)
                self.fireworks.remove((firework, x, y, step, color))
        
        self.root.after(100, self.animate_fireworks)

if __name__ == "__main__":
    root = tk.Tk()
    app = CongratulationApp(root)
    root.mainloop()
