import tkinter as tk
from tkinter import filedialog, messagebox
from utils import iconPath
import tabula
import pandas as pd
import os

enabled_companies = [""]
path = iconPath(__file__)
icon_path = path

def main_function(company_name):
    root = tk.Tk()

    file_label = tk.Label(root, text="Nenhum arquivo selecionado", fg="red")
    file_label.pack()

    def select_files():
        file_paths = filedialog.askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf")])
        if file_paths:
            file_label.config(text="Arquivos selecionados: {}".format(len(file_paths)), fg="green")
            convert_to_excel(file_paths)
        else:
            file_label.config(text="Nenhum arquivo selecionado", fg="red")

    def convert_to_excel(file_paths):
        output_folder = os.path.join(os.getcwd(), "relatorios/convertidos_excel")
        os.makedirs(output_folder, exist_ok=True)

        for file_path in file_paths:
            try:
                dfs = tabula.read_pdf(file_path, pages='all')
                output_file = os.path.join(output_folder, os.path.basename(file_path)[:-4] + ".xlsx")
                writer = pd.ExcelWriter(output_file)
                for i, df in enumerate(dfs):
                    df.to_excel(writer, sheet_name='Sheet{}'.format(i+1), index=False)
                writer.close()
                messagebox.showinfo("Conversão concluída", "Os arquivos foram convertidos com sucesso.")
            except Exception as e:
                messagebox.showerror("Erro na conversão", "Ocorreu um erro ao converter os arquivos: {}".format(e))

    select_button = tk.Button(root, text="Selecionar Arquivos", command=select_files)
    select_button.pack()

    root.mainloop()
