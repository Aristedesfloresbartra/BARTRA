
class usuarios:

    def __init__(self,id_usuarios,usuario,email,clave):
        self.id_usuarios = id_usuarios
        self.usuario = usuario
        self.email = email
        self.clave = clave

    def setId(self,id_usuarios):
        self.id_usuarios = id_usuarios
    def getId(self):
        return self.id_usuarios

    def setUsuario(self,usuario):
        self.usuario = usuario
    def getUsuario(self):
        return self.usuario

    def setEmail(self,email):
        self.email = email
    def getEmail(self):
        return self.email

    def setClave(self,clave):
        self.clave = clave
    def getClave(self):
        return self.clave