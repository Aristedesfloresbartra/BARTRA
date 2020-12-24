from modelo.estado import estado
from tkinter import messagebox

class controlArticulos:

    def __init__(self):
        pass

    def crearArticuloss(self,lista):
  
        self.enlace = estado()
        self.enlace.setDatosArticulos(lista[0],lista[1],lista[2],lista[3])
        self.enlace.setEstado(lista[4],lista[5])

        resp = self.enlace.insertarArticulos()

        if resp:
            messagebox.showinfo("Registro","Registro creado correctamente")
        else:
            messagebox.showerror("Registro","ERROR, al intentar crear el registro")

    def LeerRegistros(self,codigo):
        self.enlace = estado()
        lista = self.enlace.mostrarArticulos(codigo)
        return lista

    def ActualizarRegistro(self,codigo,producto,categoria,precio,pedidos,entrega):
        self.enlace = estado()
        self.enlace.actualizarArticulos(codigo,producto,categoria,precio,pedidos,entrega)

    def EliminarRegistro(self,codigo):

        mensaje = messagebox.askquestion("Mensaje","¿Seguro que deseas eliminar el registro?")
        if mensaje=="yes":
            self.enlace = estado()
            resp = self.enlace.eliminarArticulos(codigo)
            if resp:
                messagebox.showinfo("Eliminar","REGISTRO ELIMINADO CORRECTAMENTE")
            else:
                messagebox.showerror("Eliminar","ERROR, al intentar eliminar")
        else:
            pass