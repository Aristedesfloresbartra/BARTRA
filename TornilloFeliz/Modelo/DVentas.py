from _Entidades.venta import venta
from Modelo.Conexion import *
class Ventas(venta):

    def __init__(self):
        pass

    def setDatosVentas(self,id_venta,codigo_pro,n_venta,cantidad,precio,total):
        venta.__init__(self,id_venta,codigo_pro,n_venta,cantidad,precio,total)

    def insertarVenta(self):
        conecta = Conexion()
        conecta.conectar()
        sql = "INSERT INTO ventas(id_venta,codigo_pro,n_ventas,cantidad,precio,total)VALUES(NULL,'"+self.codigo_pro+"','"+self.n_ventas+"','"+self.cantidad+"','"+self.precio+"','"+self.total+"')"
        conecta.setEjecutaQuery(sql)
    
    def consultaNventas(self,n_ventas):
        conectar = Conexion()
        conectar.conectar()
        sql = "SELECT * FROM ventas WHERE n_ventas="+str(n_ventas)
        resultado = conectar.getEjecutaQuery()
        return resultado








