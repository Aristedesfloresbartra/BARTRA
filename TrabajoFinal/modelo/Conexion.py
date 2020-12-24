import pymysql
class Conexion():

    def __init__(self):
        self.servidor = "localhost"
        self.bd="ionsac"
        self.user = "root"
        self.password=""
        
    def conectar(self):
        try:
            self.conexion = pymysql.connect(self.servidor,self.user,self.password,self.bd)
            self.cn = self.conexion.cursor()
            return 1
        except Exception as e:
            return 0
    def setEjecutarQuery(self,sql):
        try:
            self.respuesta=self.cn.execute(sql)
            self.conexion.commit()
            self.conexion.close()
            return 1
        except Exception as e:
            self.conexion.rollback()
            return 0
    def getEjecutarQuery(self,sql):
        try:
            self.cn.execute(sql)
            registro = self.cn.fetchall()
            return registro
        except Exception as e:
            return 0