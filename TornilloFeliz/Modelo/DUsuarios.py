from _Entidades.usuarios import *
from Modelo.Conexion import *

class Usuarios(usuarios):

    def __init__(self):
        pass

    def setDatosUsuarios(self,id_usuarios,usuario,email,clave):
        usuarios.__init__(self,id_usuarios,usuario,email,clave)

    def insertarUsuarios(self):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "INSERT INTO usuario (id_usuarios,usuario,email,clave)VALUES(NULL,'"+self.usuario+"','"+self.email+"','"+self.clave+"')"
            conecta.setEjecutaQuery(sql)
        except Exception as e:
            print("Error el insertrar los datos en el modelo")

    def iniciarSession(self,usuario,clave):
        try:
            conecta = Conexion()
            conecta.conectar()
            sql = "select * from usuario where usuario='"+str(usuario)+"' and clave='"+str(clave)+"'"
            registro = conecta.getEjecutaQuery(sql)
            return registro
        except Exception as e:
            print("Error al traer los datos en el modelo")

    