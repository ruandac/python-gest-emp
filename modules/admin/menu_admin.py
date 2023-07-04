from tkinter import messagebox
from utils import iconPath

enabled_companies = [""]
path = iconPath(__file__)
icon_path = path

def main_function(company_name):
    messagebox.showinfo("Menu Administração", f"Empresa: {company_name}")
