from Modelo.DVentas import *

class controlventas():

    def registrarVentas(self,lista):
        enlace = Ventas()
        enlace.setDatosVentas(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
        enlace.insertarVenta()

    def consultaNventas(self,n_ventas):
        enlace = Ventas()
        resulatdo = enlace.consultaNventas(n_ventas)
        return resulatdo
    
































