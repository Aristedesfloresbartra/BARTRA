class persona:
    
    def __init__(self,nombre,apellidos,dni,sexo):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.sexo=sexo

    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellidos(self,apellidos):
        self.apellidos=apellidos   
    def setDni(self,dni):
        self.dni=dni
    def setSexo(self,sexo):
        self.sexo=sexo


    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getDNI(self):
        return self.dni
    def getSexo(self):
        return self.sexo