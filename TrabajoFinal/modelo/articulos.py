class articulos:

    def __init__(self,codigo,producto,categoria,precio):
        self.codigo = codigo
        self.producto = producto
        self.categoria = categoria
        self.precio = precio


    def setCodigo(self,codigo):
        self.codigo = codigo
    def setProducto(self,producto):
        self.producto = producto
    def setCategoria(self,categoria):
        self.categoria = categoria
    def setPrecio(self,precio):
        self.precio = precio

    
    def getCodigo(self):
        return self.codigo
    def getProducto(self):
        return self.producto
    def getCategoria(self):
        return self.categoria
    def getPrecio(self):
        return self.precio
