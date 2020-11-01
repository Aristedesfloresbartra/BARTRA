from .conexion import Conexion

class Articulos(Conexion):

    def __init__(self,Codigo,Nombre,Categoria,Precio,Color):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.Precio = Precio
        self.Color = Color

    def setCodigo(self,Codigo):
        self.Codigo = Codigo
    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def setCategoria(self,Categoria):
        self.Categoria = Categoria
    def setPrecio(self,Precio):
        self.Precio = Precio
    def setColor(self,Color):
        self.Color = Color

    
    def getCodigo(self):
        return self.Codigo
    def getNombre(self):
        return self.Nombre
    def getCategoria(self):
        return self.Categoria
    def getPrecio(self):
        return self.Precio
    def getColor(self):
        return self.Color


    

        
        
