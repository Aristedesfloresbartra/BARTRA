class productos:

    def __init__(self,id_productos,codigo,nombre,precio,categoria,marca):
        self.id_productos = id_productos
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.marca = marca

    def setId(self,id_productos):
        self.id_productos = id_productos
    def getId(self):
        return self.id_productos

    def setCodigo(self,codigo):
        self.codigo = codigo
    def getCodigo(self):
        return self.codigo

    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setPrecio(self,precio):
        self.nombre = precio
    def getPrecio(self):
        return self.precio

    def setCategoria(self,categoria):
        self.categoria = categoria
    def getCategoria(self):
        return self.categoria

    def setMarca(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
