from model.persona import persona
from model.Conexion import Conexion
from tkinter import messagebox

class Alumno(persona):

    codigo =""
    ciclo =""

    
    def __init__(self):
        pass

    def setDatosPersonales(self,nombre,apellidos,dni,sexo):
        persona.__init__(self,nombre,apellidos,dni,sexo)
  
        
    def setMatricula(self,codigo,ciclo):
        self.codigo=codigo
        self.ciclo=ciclo


    def setCodigo(self,codigo):
        self.codigo=codigo
    def setCiclo(self,ciclo):
        self.ciclo=ciclo


    def getCodigo(self):
        return self.codigo
    def getCiclo(self):
        return self.ciclo



    def insertarAlumnos(self):
        conecta = Conexion()
        conecta.conectar()
        SQL = "INSERT INTO alumno(codigo,nombre,apellidos,dni,sexo,ciclo)VALUES('"+self.codigo+"','"+self.nombre+"','"+self.apellidos+"','"+self.dni+"','"+self.sexo+"','"+self.ciclo+"')"
     
        resp = conecta.setEjecutarQuery(SQL)
        if resp:
            return 1
            #print("Registro correcto")
        else:
            return 0
            #print("Registro incorrecto")

    def mostrarAlumnos(self):
        conecta = Conexion()
        conecta.conectar()

        sql = "SELECT *FROM alumno"
        registros=conecta.getEjecutarQuery(sql)
        return registros

    def actualizarAlumnos(self,codigo):
        pass

    def eliminarAlumnos(self,codigo):
        pass



