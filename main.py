import tkinter as tk
from tkinter import Toplevel, ttk
from PIL import Image, ImageTk
import importlib
import keyboard

class InitialScreen(tk.Tk):
    def __init__(self, empresas):
        tk.Tk.__init__(self)

        self.title("Selecionar Empresa")
        self.geometry("400x200")

        self.empresas = empresas

        label = tk.Label(self, text="Selecione a empresa:")
        label.pack(pady=10)

        self.company_var = tk.StringVar()
        company_combobox = ttk.Combobox(self, textvariable=self.company_var, values=self.empresas, state="readonly")
        company_combobox.pack(pady=10)

        button = tk.Button(self, text="Confirmar", command=self.confirm_selection)
        button.pack(pady=10)

    def confirm_selection(self):
        selected_company = self.company_var.get()
        self.destroy()
        app = MyApp(selected_company)
        app.mainloop()

class MyApp(tk.Tk):
    def __init__(self, selected_company):
        tk.Tk.__init__(self)

        # Definir o tamanho da tela
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")

        # Calcular o tamanho da toolbar
        toolbar_height = int(height * 0.1)

        # Criar a toolbar
        self.toolbar = tk.Frame(self, bg="#ECECEC")
        self.toolbar.place(relx=0, rely=0, relwidth=1, relheight=toolbar_height/height)

        # Definir o frame principal
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.place(relx=0, rely=toolbar_height/height, relwidth=1, relheight=1-(toolbar_height/height))

        # Carregar as funções das empresas
        self.functions = {}
        self.load_functions()

        # Mostrar os botões da empresa selecionada
        self.update_buttons(selected_company)

        # Registrar o evento de pressionar a tecla F8
        keyboard.on_press_key("f8", lambda _: self.open_company_menu())

    def load_functions(self):
        # Carregar as funções das empresas e os botões habilitados
        functions = ["gerar_relatorio", "compare_relatorio", "menu_admin"]

        for function in functions:
            module = importlib.import_module(function)

            for company in module.enabled_companies:
                if company not in self.functions:
                    self.functions[company] = []

                self.functions[company].append(module)

    def update_buttons(self, selected_company):
        # Limpar os botões existentes na toolbar
        for widget in self.toolbar.winfo_children():
            widget.destroy()

        # Carregar a função e botões da empresa selecionada
        selected_functions = self.functions.get(selected_company)

        if selected_company == "Contabilidade":
            all_functions = set()
            for functions_list in self.functions.values():
                all_functions.update(functions_list)

            selected_functions = list(all_functions)

        if selected_functions:
            for module in selected_functions:
                # Carregar o ícone
                icon = Image.open(module.icon_path)
                icon = icon.resize((30, 30))  # Redimensionar o ícone para 50x50 pixels
                icon = ImageTk.PhotoImage(icon)

                # Criar o botão com o ícone e atribuir o módulo correspondente
                btn = tk.Button(
                    self.toolbar,
                    image=icon,
                    command=lambda company_name=selected_company, module=module: module.main_function(company_name),
                    width=35,
                    height=35,
                    relief=tk.RAISED
                )
                btn.image = icon  # Manter uma referência à imagem para evitar problemas de exibição
                btn.pack(side=tk.LEFT, padx=10)

        companyName = tk.Label(self.toolbar, text=selected_company, font=(20), bg="#ECECEC", padx=10)
        companyName.pack(side=tk.RIGHT)

    def open_company_menu(self):
        self.select_menu = Toplevel(self)  
        self.select_menu.geometry("400x200")  
        label = tk.Label(self.select_menu, text="Selecione a empresa:")
        label.pack(pady=10)

        self.select_menu.company_var = tk.StringVar()
        company_combobox = ttk.Combobox(self.select_menu, textvariable=self.select_menu.company_var, values=empresas, state="readonly")
        company_combobox.pack(pady=10)

        selected_company = self.select_menu.company_var.get()

        button = tk.Button(self.select_menu, text="Confirmar", command=self.confirm_selection)
        button.pack(pady=10)

    def confirm_selection(self):
        self.update_buttons(self.select_menu.company_var.get())
        self.select_menu.destroy()


if __name__ == "__main__":
    empresas = [
        "Contabilidade",
        "Fricat",
    ]

    initial_screen = InitialScreen(empresas)
    initial_screen.mainloop()
