import tkinter as tk
import pymysql
from tkinter import ttk,messagebox
from controlador.controlArticulos import controlArticulos
from modelo.Conexion import Conexion

class n_registro(ttk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.MiCod = tk.StringVar()
        self.MiPro = tk.StringVar()
        self.MiCad = tk.StringVar()
        self.MiPre = tk.StringVar()
        self.MiPed = tk.StringVar()
        self.MiEnt = tk.StringVar()

        self.Label()
        self.Entradas()
        self.Checks()
        self.Botones()
        self.Tree()

    def Label(self):
        ######## ETIQUETAS LABEL ######################
        self.codigo = tk.Label(self,text="Codigo")
        self.codigo.grid(row=0,column=0)
        self.codigo.config(fg="black",font=("Arial",12)) 


        self.producto = tk.Label(self,text="Producto")
        self.producto.grid(row=1,column=0)
        self.producto.config(fg="black",font=("Arial",12)) 

        self.categoria = tk.Label(self,text="Categoria")
        self.categoria.grid(row=2,column=0)
        self.categoria.config(fg="black",font=("Arial",12)) 

        self.precio = tk.Label(self,text="Precio")
        self.precio.grid(row=3,column=0)
        self.precio.config(fg="black",font=("Arial",12)) 

        self.c_pedidos = tk.Label(self,text="Pedidos")
        self.c_pedidos.grid(row=4,column=0)
        self.c_pedidos.config(fg="black",font=("Arial",12)) 

        self.fecha_entrega = tk.Label(self,text="Entrega")
        self.fecha_entrega.grid(row=5,column=0)
        self.fecha_entrega.config(fg="black",font=("Arial",12)) 
        ############################################################
    def Entradas(self):

        ######## CAJAS DE TEXTO ###################################
        self.caja_codigo = tk.Entry(self,width=30,textvariable=self.MiCod)
        self.caja_codigo.grid(row=0,column=1,padx=15, pady=5,ipady=4)
        self.caja_codigo.config(state='normal')

        self.caja_producto = tk.Entry(self,width=30,textvariable=self.MiPro)
        self.caja_producto.grid(row=1,column=1,padx=15, pady=5,ipady=4)

        self.caja_categoria = tk.Entry(self,width=30,textvariable=self.MiCad)
        self.caja_categoria.grid(row=2,column=1,padx=15, pady=5,ipady=4)

        self.caja_precio = tk.Entry(self,width=30,textvariable=self.MiPre)
        self.caja_precio.grid(row=3,column=1,padx=15, pady=5,ipady=4)

        self.caja_pedidos = tk.Entry(self,width=30,textvariable=self.MiPed)
        self.caja_pedidos.grid(row=4,column=1,padx=15, pady=5,ipady=4)
        self.caja_pedidos.config(state='disabled')

        self.caja_entrega = tk.Entry(self,width=30,textvariable=self.MiEnt)
        self.caja_entrega.grid(row=5,column=1,padx=15, pady=5,ipady=4)
        self.caja_entrega.config(state='disabled')

        ################################################################
    def Checks(self):
        ############# CKECK ###########################################
        self.codigo_c = tk.IntVar()

        self.checkbox_codigo = ttk.Checkbutton(self,text="",variable=self.codigo_c,command=self.ckeckCodigo)
        self.checkbox_codigo.grid(row=0,column=2)
        
        self.pedidos_c = tk.IntVar()
        self.pedidos_check = ttk.Checkbutton(self,text="",variable=self.pedidos_c,command=self.ckeckPedidos)
        self.pedidos_check.grid(row=4,column=2)

        self.entrega_c = tk.IntVar()
        self.entrega_check = ttk.Checkbutton(self,text="",variable=self.entrega_c,command=self.ckeckEntrega)
        self.entrega_check.grid(row=5,column=2)
        ##############################################################

    def Registro(self):
        if len(self.MiCod.get() and self.MiPro.get() and self.MiCad.get() and self.MiPre.get())!=0:

            self.datos_numeros = (self.MiCod.get()+ self.MiPre.get())
            if self.datos_numeros.isdigit()==True:

                self.lista = (self.MiCod.get(),self.MiPro.get(),self.MiCad.get(),self.MiPre.get(),self.MiPed.get(),self.MiEnt.get())
                self.enlace = controlArticulos()
                self.enlace.crearArticuloss(self.lista)
                self.Limpiar()
            else:
                messagebox.showwarning("Upp¡","Porfavor ingresé solo números en el campo CODIGO Y PRECIO")
        else:
            messagebox.showerror("Error","¡Los 4 primeros campos son obligatorio!")

        self.Tree()
    def Limpiar(self):
        self.MiCod.set("")
        self.MiPro.set("")
        self.MiCad.set("")
        self.MiPre.set("")
        self.MiPed.set("")
        self.MiEnt.set("")  
    def Consulta(self):

        self.Registros = controlArticulos()
        self.leerRegistros=self.Registros.LeerRegistros(self.MiCod.get())
        if self.leerRegistros:
            for articulos in self.leerRegistros:
                self.MiCod.set(articulos[0])
                self.MiPro.set(articulos[1])
                self.MiCad.set(articulos[2])
                self.MiPre.set(articulos[3])
                self.MiPed.set(articulos[4])
                self.MiEnt.set(articulos[5])
        else:
            messagebox.showinfo("Info","No se encontraron registro del CODIGO '{}' ".format(self.MiCod.get()))
    def Editar(self):

        if len(self.MiPro.get()and self.MiCad.get()and self.MiPre.get()and self.MiPed.get()and self.MiEnt.get())!=0:
            self.enlace = controlArticulos()
            self.enlace.ActualizarRegistro(self.MiCod.get(),self.MiPro.get(),self.MiCad.get(),self.MiPre.get(),self.MiPed.get(),self.MiEnt.get())
            messagebox.showinfo("Edicion","¡Edicion correcta!")
            self.Consulta()
            self.Tree()
        else:
            messagebox.showwarning("Advertencia","Porfavor realize la consulta antes")
    def Eliminar(self):

        if len(self.MiCod.get())!=0:
            self.enlace = controlArticulos()
            self.enlace.EliminarRegistro(self.MiCod.get())
            self.Tree()
        else:
            messagebox.showinfo("Info","Porfavor ingrese el codigo")

    def Botones(self):
        ######### BOTONES ###########################################
        self.eventos = controlArticulos()
        self.boton_crear = tk.Button(self,text="             CREAR              ",command=self.Registro)
        self.boton_crear.place(x=10,y=230)

        self.boton_editar = tk.Button(self,text="              EDITAR               ",command=self.Editar)
        self.boton_editar.place(x=150,y=230)

        self.boton_eliminar = tk.Button(self,text="          ELIMINAR           ",command=self.Eliminar)
        self.boton_eliminar.place(x=10,y=260)

        self.boton_consulta = tk.Button(self,text="          CONSULTAR         ",command=self.Consulta)
        self.boton_consulta.place(x=150,y=260)

        self.boton_limpiar = tk.Button(self,text="      \t\tLIMPIAR\t\t\t        ",command=self.Limpiar)
        self.boton_limpiar.place(x=10,y=290)
        #############################################################
    def Tree(self):

        self.style = ttk.Style(self)
        self.style.configure("Treeview", rowheight=30)

        self.treev = ttk.Treeview(self, selectmode ='browse') 
        self.treev.place(x=340,y=0)

        self.verscrlbar = ttk.Scrollbar(self, orient ="vertical", command = self.treev.yview) 
        self.verscrlbar.place(x=320,y=120) 
        self.treev.configure(xscrollcommand = self.verscrlbar.set) 

        self.treev["columns"] = ("1", "2", "3","4","5","6") 
        self.treev['show'] = 'headings'

        self.treev.column("1", width = 106, anchor ='c') 
        self.treev.column("2", width = 106, anchor ='c') 
        self.treev.column("3", width = 106, anchor ='c')
        self.treev.column("4", width = 106, anchor ='c') 
        self.treev.column("5", width = 106, anchor ='c') 
        self.treev.column("6", width = 106, anchor ='c') 
                    
        self.treev.heading("1", text ="CODIGO") 
        self.treev.heading("2", text ="PRODUCTO") 
        self.treev.heading("3", text ="CATEGORIA") 
        self.treev.heading("4", text ="PRECIO") 
        self.treev.heading("5", text ="PEDIDOS") 
        self.treev.heading("6", text ="ENTREGA") 



        self.registros = self.treev.get_children()

        for self.registro in self.registros:
            self.treev.delete(self.registro)

        self.conexion = pymysql.connect(host="localhost",user="root",password="",database="ionsac")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("select * from articulos")
        
        self.datos = self.MiCod.get(),self.MiPro.get(),self.MiCad.get(),self.MiPre.get(),self.MiPed.get(),self.MiEnt.get()

        for self.datos in self.cursor:
            self.treev.insert('',0,text="lb",value=(self.datos))



    def ckeckCodigo(self):

        if(self.codigo_c.get()==0):
            self.caja_codigo.config(state='normal')
        else:
            self.caja_codigo.config(state='disabled')
    def ckeckPedidos(self):
    
        if(self.pedidos_c.get()==0):
            self.caja_pedidos.config(state='disabled')
        else:
            self.caja_pedidos.config(state='normal')
    def ckeckEntrega(self):
    
        if(self.entrega_c.get()==0):
            self.caja_entrega.config(state='disabled')
        else:
            self.caja_entrega.config(state='normal')

