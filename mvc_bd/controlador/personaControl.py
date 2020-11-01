from model.alumno import Alumno

class personaControl:

    def __init__(self):
        pass

# crear registro
    def crearRegistro(self,lista):

        self.enlace=Alumno()
        self.enlace.setDatosPersonales(lista[0],lista[1],lista[2],lista[3])
        self.enlace.setMatricula(lista[4],lista[5])
    
        resp = self.enlace.insertarAlumnos()

        if resp:
            print("correcto")
        else:
            print("Incorrecto")
# leer registro
    def leerRegistro(self):
        self.enlace = Alumno()
        lista = self.enlace.mostrarAlumnos()
        return lista

# actualizar registro
    def actualizarRegistro(self,codigo):
        pass

# eliminar registro
    def eliminarRegistro(self,codigo):
        pass