import tkinter as tk
from tkinter import ttk
import pymysql
from Modelo.Articulos import Articulos
from tkinter import messagebox


class ControlArticulos(Articulos):
    
    def __init__(self,Codigo,Nombre,Categoria,Precio,Color):
        Articulos.__init__(self,Codigo,Nombre,Categoria,Precio,Color)

    def crearArtiulos(self):
        
        if len(self.Codigo.get() and self.Nombre.get() and self.Categoria.get() and self.Precio.get() and self.Color.get())!=0:
            
            self.numDigit = (self.Codigo.get()+ self.Precio.get())

            if self.numDigit.isdigit()==True:

                try:
                    self.conexion = pymysql.connect(host="localhost",user="root",password="",database="productos")
                    self.cursor=self.conexion.cursor()

                    self.cursor.execute("insert into articulos values(%s,%s,%s,%s,%s)",(
                                                    self.Codigo.get(),
                                                    self.Nombre.get(),
                                                    self.Categoria.get(),
                                                    self.Precio.get(),
                                                    self.Color.get())                                
                                                            )
                    self.conexion.commit()
                    self.conexion.close()
                    messagebox.showinfo("Registo","Registro creado correctamente")
                    self.Limpiar()
                except(pymysql.err.IntegrityError):
                    messagebox.showerror("Error","El codigo {} ya existe".format(self.Codigo.get()))

            else:
                messagebox.showwarning("Advertencia","¡Ingrese solo numero en el campo CODIGO Y PRECIO!")
        else:
            messagebox.showwarning("Advertencia","Debes rellenar todos los campos")

  
    
        ############################

    def EditarArticulos(self):
        if len(self.Codigo.get())!=0:
            self.numCodigo = self.Codigo.get()
            if self.numCodigo.isdigit()==True:
    
                if len(self.Nombre.get() and self.Categoria.get() and self.Precio.get() and self.Color.get())!=0:
                    self.conexion = pymysql.connect(host="localhost",user="root",password="",database="productos")
                    self.cursor=self.conexion.cursor()

                    self.cursor.execute("select * from articulos where codigo=" + self.Codigo.get())
                    self.articulos = self.cursor.fetchall()
                    if self.articulos:
                        self.Update_sql = ("UPDATE articulos SET nombre=%s,categoria=%s,precio=%s,color=%s WHERE codigo=" + self.Codigo.get())
                        self.IngresarDatos = (self.Nombre.get(),self.Categoria.get(),self.Precio.get(),self.Color.get())
                        self.cursor.execute(self.Update_sql,self.IngresarDatos)

                        self.conexion.commit()
                        self.conexion.close()
                        messagebox.showinfo("Edicion","El registro se editó correctamente")
                        self.Consulta()
                    else:
                        messagebox.showerror("Error","¡Error en la consulta no se encontro el registro {} !".format(self.Codigo.get()))
                else:
                    messagebox.showwarning("Advertencia","Por seguridad realize la CONSULTA")
            else:
                messagebox.showerror("Error","¡Ingresé solo numero en el campo CODIGO!")
        else:
            messagebox.showwarning("Advertencia","¡Ingresé el codigo para editar los articulos!")

    def EliminarArticulos(self):

        if len(self.Codigo.get())!=0:
            
            self.numCodigo = self.Codigo.get()
            if self.numCodigo.isdigit()==True:

                self.mensaje = messagebox.askquestion("Borrar","¿Seguro que quires eliminar el registro '{}' ?".format(self.Nombre.get()))
                
                if self.mensaje=="yes":
                    self.conexion = pymysql.connect(host="localhost",user="root",password="",database="productos")
                    self.cursor=self.conexion.cursor()

                    self.cursor.execute("select * from articulos where codigo=" + self.Codigo.get())
                    self.articulos = self.cursor.fetchall()
                    if self.articulos:
                        self.cursor.execute("DELETE FROM articulos WHERE Codigo=" + self.Codigo.get())
                        self.conexion.commit()
                        messagebox.showinfo("Eliminar","El registro se elimino correctamente")
                        self.Limpiar() 
                    else:
                        messagebox.showerror("Error","Error al eliminar NO SE ENCONTRO EL REGISTRO '{}' ".format(self.Codigo.get()))
                else:
                    pass
            else:
                messagebox.showerror("Error","¡Solo puedes ingresar numero en el campo codigo!")    
        else:
            messagebox.showwarning("Advertencia","¡Debes ingresar el codigo del articulo para eliminar!")
        
    def Consulta(self):
        
        if len(self.Codigo.get())!=0:
            
            codigoNum= self.Codigo.get()
            while codigoNum.isdigit()==False: 
                messagebox.showerror("Error","¡Solo puedes ingresar numero en el campo codigo!")
                break

            self.conexion = pymysql.connect(host="localhost",user="root",password="",database="productos")
            self.cursor=self.conexion.cursor()
            self.cursor.execute("select * from articulos where codigo=" + self.Codigo.get())

            self.articulos = self.cursor.fetchall()


            if self.articulos:
                for articulo in self.articulos:
                    self.Codigo.set(articulo[0])
                    self.Nombre.set(articulo[1])
                    self.Categoria.set(articulo[2])
                    self.Precio.set(articulo[3])
                    self.Color.set(articulo[4])
                self.conexion.commit()
            else:
                messagebox.showinfo("Info","No se encontraron registro del CODIGO '{}' ".format(self.Codigo.get()))
        else:
            messagebox.showwarning("Advertencia","¡Ingrese el codigo del articulos para realizar la consulta!")

    def Limpiar(self):
        self.Codigo.set("")
        self.Nombre.set("")
        self.Categoria.set("")
        self.Precio.set("")
        self.Color.set("")




        
       



