import pymysql

class Conexion:

    def __init__(self):
        self.servidor="localhost"
        self.bd="senati"
        self.user="root"
        self.clave=""

    def conectar(self):
        try:
            self.conexion=pymysql.connect(self.servidor,self.user,self.clave,self.bd)
            self.cn= self.conexion.cursor()
            
            print("se conecto a la base de datos")

        except Exception as e:
            print("Error",e)

        
    def setEjecutarQuery(self,sql):
        try:
            respusta = self.cn.execute(sql)
            self.conexion.commit()
            self.conexion.close()
            return 1

        except Exception as e:
            print("Erre",e)
            self.conexion.rollback()
            return 0

    def getEjecutarQuery(self,sql):
        try:
            self.cn.execute(sql)
            registros = self.cn.fetchall()
            return registros
        except Exception as e:
            return 0



        
        
            

