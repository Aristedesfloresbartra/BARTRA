import tkinter as tk
from tkinter import ttk

from Vista.aplicacion_interfaz import Notebook_listado,Notebook_registro

class Aplicacion(ttk.Frame):
    
    def __init__(self, ventana_principal):
        super().__init__(ventana_principal)
        ventana_principal.title("Registro de productos")
        ventana_principal.resizable(False,False)

        
        self.notebook = ttk.Notebook(self)

        #Notebook  de la interfaz crear usuario by aristedes
        self.N_registro = Notebook_registro(self.notebook)
        self.notebook.add(
            self.N_registro, text="Control de productos", padding=10)

        #Notebook de la interfaz Listado productos
        
        self.N_listado = Notebook_listado(self.notebook)
        self.notebook.add(
            self.N_listado, text="Lista de productos", padding=10) 
        
        self.notebook.pack(padx=0, pady=0)
        self.notebook.config(width="720", height="360")
       
        self.pack(fill="x")


ventana_principal = tk.Tk()
app = Aplicacion(ventana_principal)
app.mainloop()