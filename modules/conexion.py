import sqlite3

class Conexion():
    def __init__(self):
        self.Database="db/inventario2.db"
        self.conexion=sqlite3.connect(self.Database)
        self.cursor=self.conexion.cursor()

    def CloseConexion(self):
        self.conexion.commit()
        self.conexion.close()

    