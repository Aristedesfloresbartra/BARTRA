from Modelo.DProductos import *

class controlProductos():

    def insertarProductos(self,lista):
        try:
            enlace = Productos()
            enlace.setDatosProductos(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
            enlace.insertarProductos()
        except Exception as e:
            print("Ha ocurrido un error al intentar registrar en el controlador")

    def validarCodigo(self,codigo):
        try:
            enlace = Productos()
            codigo = enlace.validarCodigo(codigo)
            return codigo
        except Exception as e:
            print("Error al traer el codigo en el controlador")

    def tablaProductos(self):
        try:
            enlace = Productos()
            resultado = enlace.tablaProductos()
            return resultado
        except Exception as e:
            print("Error al traer los datos de la tabla en el controlador")

    def buscarProductos(self,valor):

        try:
            enlace = Productos()
            valor = enlace.buscarProductos(valor)
            return valor

        except Exception as e:
            print("Error en el controlador al realizar la busqueda")

    def editarProductos(self,listaE):
        try:
            enlace = Productos()
            enlace.setDatosProductos(listaE[0],listaE[1],listaE[2],listaE[3],listaE[4],listaE[5])
            enlace.editarProductos()
        except Exception as e:
            print("Error al interntar editar en el controlador")

    def consultaId(self,id_productos):
        try:
            enlace = Productos()
            id_producto=enlace.consultaId(id_productos)
            return id_producto
        except Exception as e:
            print("Error en el controlador (consulta)")

    def eliminarProductos(self,listaEli):
        try:
            enlace = Productos()
            enlace.setDatosProductos(listaEli[0],listaEli[1],listaEli[2],listaEli[3],listaEli[4],listaEli[5])
            enlace.eliminarProductos()
        except Exception as e:
            print("Ha ocurrido un error en el controlador al intentar eliminar")

    def eliminarProductosFila(self,value):
        try:
            enlace = Productos()
            enlace.eliminarProductosFila(valor=(value))
        except Exception as e:
            print("Ha ocurrido un error en el controlador al intentar eliminar")

    def consultaPrecioP(self,codigo,precio):
        enlace = Productos()
        pre = enlace.consultaPrecio(codigo,precio)
        return pre