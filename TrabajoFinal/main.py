import tkinter as tk
from tkinter import ttk
from vista.interfaz import n_registro

class Aplicacion(ttk.Frame):

    def __init__(self,root):
        super().__init__(root) 
        root.title("Datos")
        root.resizable(False,False)

        self.notebook = ttk.Notebook(self)
        self.n_registro = n_registro(self.notebook)
        self.notebook.add(self.n_registro,text="REGISTRO DE DATOS",padding=10)

        self.notebook.pack(padx=0, pady=0)
        self.notebook.config(width="1000", height="360")
        self.pack(fill="x")
        

root = tk.Tk()
app = Aplicacion(root)

app.mainloop()
