from Modelo.DUsuarios import *

class controlUsuario():


    def insertarUsuarios(self,lista):
        try:
            self.enlace = Usuarios()
            self.enlace.setDatosUsuarios(lista[0],lista[1],lista[2],lista[3])
            self.enlace.insertarUsuarios()
        except Exception as e:
            print("Error al intentar registrar los datos en el controlador")

    def iniciarSession(self,usuario,clave):
        try:
            self.enlace = Usuarios()
            registro = self.enlace.iniciarSession(usuario,clave)
            return registro
        except Exception as e:
            print("Error al traer los datos en el controlador")

