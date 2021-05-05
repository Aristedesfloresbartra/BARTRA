
class venta:

    def __init__(self,id_venta,codigo_pro,n_ventas,cantidad,precio,total):

        self.id_venta = id_venta
        self.codigo_pro = codigo_pro
        self.n_ventas = n_ventas
        self.cantidad = cantidad
        self.precio = precio
        self.total = total

    def setIdventa(self,id_venta):
        self.id_venta = id_venta
    def getIdventa(self):
        return self.id_venta

    def setCodigo_pro(self,codigo_pro):
        self.codigo_pro = codigo_pro
    def getCodigo_pro(self):
        return self.codigo_pro

    def setNventas(self,n_ventas):
        self.n_ventas = n_ventas
    def getNventas(self):
        return self.n_ventas

    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def getCantidad(self):
        return self.cantidad

    def setProcio(self,precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio

    def setTotal(self,total):
        self.total = total
    def getTotal(self):
        return self.total

    