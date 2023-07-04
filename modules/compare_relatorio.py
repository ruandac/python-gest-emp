from tkinter import messagebox
from utils import iconPath

enabled_companies = ["Fricat"]
path = iconPath(__file__)
icon_path = path

def main_function(company_name):
    messagebox.showinfo("Comparar Relatorios", f"Comparar Relatorios: {company_name}")
