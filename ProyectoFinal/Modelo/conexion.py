import pymysql

class Conexion():

    def __init__(self):
        self.servidor="localhost"
        self.bd="productos"
        self.user="root"
        self.clave=""

    def conectar(self):
        try:
            self.conexion=pymysql.connect(self.servidor,self.user,self.clave,self.bd)
            self.cn= self.conexion.cursor()
            
            print("se conecto a la base de datos")

        except Exception as e:
            print("Error",e)

        finally:
            self.conexion.close()