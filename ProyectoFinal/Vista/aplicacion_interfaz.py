import tkinter as tk
import pymysql
from tkinter import ttk,messagebox
from Controlador.control_articulos import ControlArticulos
from Modelo.Articulos import Articulos

class Notebook_registro(ttk.Frame):
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.MiCodigo = tk.StringVar()
        self.MiProducto = tk.StringVar()
        self.MiCategoria = tk.StringVar()
        self.MiPrecio = tk.StringVar()
        self.MiColor = tk.StringVar()
        
        self.objArticulos = Articulos(self.MiCodigo,self.MiProducto,self.MiCategoria,self.MiPrecio,self.MiColor)
        self.objControlButton = ControlArticulos(self.MiCodigo,self.MiProducto,self.MiCategoria,self.MiPrecio,self.MiColor)

        ############################################################################################
        self.label_codigo = ttk.Label(self,text="CODIGO")
        self.label_codigo.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.label_codigo.config(font=("Courier", 13, "italic"))


        self.caja_codigo = ttk.Entry(self,textvariable=self.objArticulos.getCodigo(),width=50)
        self.caja_codigo.grid(row=0, column=0, sticky="nsew", padx=120, pady=10,ipady=4)
        self.caja_codigo.config(state='disabled')
       
        
        self.select = tk.IntVar()
        self.checkbox = ttk.Checkbutton(self,text="",variable=self.select,command=self.checkSelect)
        self.checkbox.place(x=430, y=25)

        ############################################################################################

        self.labelNombre = ttk.Label(self,text="PRODUCTO")
        self.labelNombre.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.labelNombre.config(font=("Courier", 13, "italic"))

        self.caja_Nombre = ttk.Entry(self,textvariable=self.objArticulos.getNombre(),width=50)
        self.caja_Nombre.grid(row=1, column=0, sticky="nsew", padx=120, pady=10,ipady=4)

        self.labelCategoria = ttk.Label(self,text="CATEGORIA")
        self.labelCategoria.grid(row=2, column=0, sticky="nsew", padx=20, pady=20)
        self.labelCategoria.config(font=("Courier", 13, "italic"))

        self.caja_Categoria = ttk.Entry(self,textvariable=self.objArticulos.getCategoria(),width=50)
        self.caja_Categoria.grid(row=2, column=0, sticky="nsew", padx=120, pady=10,ipady=4)

        self.labelPrecio = ttk.Label(self,text="PRECIO")
        self.labelPrecio.grid(row=3, column=0, sticky="nsew", padx=20, pady=20)
        self.labelPrecio.config(font=("Courier", 13, "italic"))

        self.caja_Precio = ttk.Entry(self,textvariable=self.objArticulos.getPrecio(),width=50)
        self.caja_Precio.grid(row=3, column=0, sticky="nsew", padx=120, pady=10,ipady=4)


        self.labelColor = ttk.Label(self,text="COLOR P.")
        self.labelColor.grid(row=4, column=0, sticky="nsew", padx=20, pady=20)
        self.labelColor.config(font=("Courier", 13, "italic"))

        self.caja_Color = ttk.Entry(self,textvariable=self.objArticulos.getColor(),width=50)
        self.caja_Color.grid(row=4, column=0, sticky="nsew", padx=120, pady=10,ipady=4)

        ########################################################################################

        ##### BUTTON ###########################################################################

        self.boton_crear = ttk.Button(self,text="   CREAR ARTICULO   ",command=self.objControlButton.crearArtiulos)
        self.boton_crear.grid(row=0, sticky="w", column=3, padx=0,ipady=4)
     
    

        self.boton_editar = ttk.Button(self,text="   EDITAR ARTICULO   ",command=self.objControlButton.EditarArticulos)
        self.boton_editar.grid(row=1,sticky="w", column=3, padx=0,ipady=4)

        self.boton_eliminar = ttk.Button(self,text="ELIMINAR ARTICULO ",command=self.objControlButton.EliminarArticulos)
        self.boton_eliminar.grid(row=2,sticky="w",column=3, padx=0,ipady=4)

        self.boton_Limpar = ttk.Button(self,text="           LIMPIAR            ",command=self.objControlButton.Limpiar)
        self.boton_Limpar.grid(row=3,sticky="w", column=3, padx=0,ipady=4)

        self.boton_aceptar = ttk.Button(self,text="          CONSULTA        ",command=self.objControlButton.Consulta)
        self.boton_aceptar.grid(row=4,sticky="w", column=3, padx=0,ipady=4)      


    def checkSelect(self):

        if(self.select.get()==0):
            self.caja_codigo.config(state='disabled')
        else:
            self.caja_codigo.config(state='normal')
            

class Notebook_listado(ttk.Frame):

   
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)  

        self.objn_r = Notebook_registro(self)

        self.treev = ttk.Treeview(self, selectmode ='browse') 
        self.treev.pack(side ='right',ipady=14) 

        self.verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.treev.yview) 
        self.verscrlbar.pack(side ='right', fill ='x') 

        self.treev.configure(xscrollcommand = self.verscrlbar.set) 
        self.treev["columns"] = ("1", "2", "3","4","5") 
        self.treev['show'] = 'headings'

        self.treev.column("1", width = 137, anchor ='c') 
        self.treev.column("2", width = 137, anchor ='c') 
        self.treev.column("3", width = 137, anchor ='c')
        self.treev.column("4", width = 137, anchor ='c') 
        self.treev.column("5", width = 137, anchor ='c') 
                    
        self.treev.heading("1", text ="CODIGO") 
        self.treev.heading("2", text ="PRODUCTO") 
        self.treev.heading("3", text ="CATEGORIA") 
        self.treev.heading("4", text ="PRECIO") 
        self.treev.heading("5", text ="COLOR.P") 

 
        self.mostrar_datos()

    
    
    def mostrar_datos(self):
    
        self.registros = self.treev.get_children()

        for self.registro in self.registros:
            self.treev.delete(self.registro)

        self.conexion = pymysql.connect(host="localhost",user="root",password="",database="productos")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("select * from articulos")
        
        self.datos = self.objn_r.MiCodigo.get(),self.objn_r.MiProducto.get(),self.objn_r.MiCategoria.get(),self.objn_r.MiPrecio.get(),self.objn_r.MiColor.get()

        for self.datos in self.cursor:
            self.treev.insert('',0,text="lb",value=(self.datos))

   