import sqlite3

class Conexion():

    def conectar(self):
        try:
            self.conexion = sqlite3.connect("Modelo/database/usuarios.db")
            self.cursor = self.conexion.cursor()
            return 1
        except Exception as e:
            return 0
            print("Error al conectar la base de datos",e)

    def setEjecutaQuery(self,sql):
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            self.conexion.close()
            return 1
        except Exception as e:
            self.conexion.rollback()
            print("Error al procesar la informacion de la db",e)
            return 0

    def getEjecutaQuery(self,sql):
        try:
            self.cursor.execute(sql)
            registro = self.cursor.fetchall()
            return registro
        except Exception as e:
            print("Error al obtener los datos ")
            return 0

    def setEjecutaQueryDatos(self,sql,valores=()):
        try:
            self.cursor.execute(sql,valores)
            self.conexion.commit()
            self.conexion.close()
            return 1
        except Exception as e:
            self.conexion.rollback()
            print("Error al procesar la informacion de la db",e)
            return 0

