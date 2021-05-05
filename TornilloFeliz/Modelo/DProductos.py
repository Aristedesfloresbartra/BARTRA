from _Entidades.productos import *
from Modelo.Conexion import *

class Productos(productos):
    
    def __init__(self):
        pass

    def setDatosProductos(self,id_producto,codigo,nombre,precio,categoria,marca):
        productos.__init__(self,id_producto,codigo,nombre,precio,categoria,marca)

    def insertarProductos(self):

        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "INSERT INTO productos(id_productos,codigo,nombre,precio,categoria,marca)VALUES(NULL,'"+self.codigo+"','"+self.nombre+"','"+self.precio+"','"+self.categoria+"','"+self.marca+"')"
            conecta.setEjecutaQuery(sql)
        except Exception as e:
            print("Ha ocurrido un errror al intentar registrar en el modelo")

    def validarCodigo(self,codigo):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "SELECT * FROM productos WHERE codigo="+str(codigo)
            resultado = conecta.getEjecutaQuery(sql)
            return resultado

        except Exception as e:
            print("Error al traer el codigo en el modelo")

    def tablaProductos(self):

        try:   
            conecta = Conexion()
            conecta.conectar()
            sql = "SELECT * FROM productos"
            resultado = conecta.getEjecutaQuery(sql)
            return resultado
        except Exception as e:
            print("Error al traer los datos de la tabla")
    
    def buscarProductos(self,valor):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "select * from productos where id_productos like'"'%'+str(valor)+'%'"' or codigo like'"'%'+str(valor)+'%'"' or nombre like'"'%'+str(valor)+'%'"'or precio like'"'%'+str(valor)+'%'"' or categoria like'"'%'+str(valor)+'%'"'or marca like'"'%'+str(valor)+'%'"'"
            resultado = conecta.getEjecutaQuery(sql)
            return resultado

        except Exception as e:
            print("Error en la busque en el modelo")

    def editarProductos(self):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = ("UPDATE productos SET codigo='"+self.codigo+"',nombre='"+self.nombre+"',precio='"+self.precio+"',categoria='"+self.categoria+"',marca='"+self.marca+"' WHERE id_productos='"+self.id_productos+"'")
            conecta.setEjecutaQuery(sql)
        except Exception as e:
            print("Error al intentar editar en el modelo")

    def consultaId(self,id_producto):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "SELECT * FROM productos WHERE id_productos="+str(id_producto)
            resultado = conecta.getEjecutaQuery(sql)
            return resultado
        except Exception as e:
            print("Error en el modelo(consulta)")

    def eliminarProductos(self):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "DELETE FROM productos WHERE id_productos='"+self.id_productos+"'"
            conecta.setEjecutaQuery(sql)
        except Exception as e:
            print("Ha ocurrido un error al intentar eliminar en el modelo")

    def eliminarProductosFila(self,valor):

        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "DELETE FROM productos WHERE id_productos=? and codigo=? and nombre=? and precio=? and categoria=? and marca=?"
            conecta.setEjecutaQueryDatos(sql,valores=(valor))
        except Exception as e:
            print("Ha ocurrido un error al intentar eliminar en el modelo")
        
    def consultaPrecio(self,codigo,precio):
        conectar = Conexion()
        conectar.conectar()
        sql = "select * from productos where codigo='"+str(codigo)+"' and precio='"+str(precio)+"'"
        resultado = conectar.getEjecutaQuery(sql)
        return resultado












