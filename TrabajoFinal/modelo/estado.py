from modelo.articulos import articulos
from modelo.Conexion import Conexion
from tkinter import messagebox
class estado(articulos):
    pedidos = ""
    entregado = ""
    def __init__(self):
        pass

    def setDatosArticulos(self,codigo,producto,categoria,precio):
        articulos.__init__(self,codigo,producto,categoria,precio)

    def setEstado(self,pedidos,entregado):
        self.pedidos = pedidos
        self.entregado = entregado

    def setPedidos(self,pedidos):
        self.pedidos = pedidos
    def setEntregado(self,entregado):
        self.entregado = entregado
        
    def getPedidos(self):
        return self.pedidos
    def getEntregado(self):
        return self.entregado

    def insertarArticulos(self):
        conecta = Conexion()
        conecta.conectar()
        SQL = "INSERT INTO articulos(codigo,producto,categoria,precio,pedidos,entrega)VALUES('"+self.codigo+"','"+self.producto+"','"+self.categoria+"','"+self.precio+"','"+self.pedidos+"','"+self.entregado+"')"
        resp = conecta.setEjecutarQuery(SQL)
        if resp:
            return 1
        else:
            return 0
            
    def mostrarArticulos(self,codigo):
        conecta = Conexion()
        conecta.conectar()
        SQL = ("SELECT * FROM articulos WHERE codigo="+str(codigo))
        registros = conecta.getEjecutarQuery(SQL)
        return registros
        
    def actualizarArticulos(self,codigo,producto,categoria,precio,pedidos,entrega):
        conecta = Conexion()
        conecta.conectar()
        SQL = ("UPDATE articulos SET producto='"+str(producto)+"',categoria='"+str(categoria)+"',precio='"+str(precio)+"',pedidos='"+str(pedidos)+"',entrega='"+str(entrega)+"' WHERE codigo="+str(codigo))
        conecta.setEjecutarQuery(SQL)

    def eliminarArticulos(self,codigo):
        conecta = Conexion()
        conecta.conectar()
        sql_validacion = "SELECT *FROM articulos WHERE codigo="+str(codigo)
        registros= conecta.getEjecutarQuery(sql_validacion)
        if registros:
            SQL = "DELETE FROM articulos WHERE codigo="+str(codigo)
            resp = conecta.setEjecutarQuery(SQL)
            if resp:
                return 1
            else:
                return 0
        else:
            pass